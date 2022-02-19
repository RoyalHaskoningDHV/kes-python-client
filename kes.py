"""This module offers client functionality for accessing assets and properties through the abstraction provided by the table class.

Classes:
    Table: Rows represent assets and columns properties.
"""

from dataclasses import dataclass
from functools import reduce
from io import BufferedIOBase
import logging
from typing import Generator, List, Generic, Mapping, Optional, TypeVar, get_args
from uuid import UUID, uuid4

import grpc
from table_pb2 import ReadTableRequest

from table_pb2_grpc import TableStub

RowType = TypeVar('RowType')


@dataclass
class RowElement(Generic[RowType]):
    """ Associates a row with an asset """
    row: RowType
    asset_id: UUID


ParticipantType = TypeVar('ParticipantType')


@dataclass
class RowReference(Generic[ParticipantType]):
    """ Opaque class which represents a reference to a table row """
    asset_type_id: UUID
    asset_id: UUID


class Table(Generic[RowType]):
    """
    This class acts as a container for rows.
    Each instance maps to a asset type, with rows corresponding to assets.

    Type parameters:
        RowType: The type of rows hold by this class.
    """

    __channel: grpc.Channel = grpc.insecure_channel('localhost:50051')
    __stub = TableStub(__channel)

    _asset_type_id: UUID
    _rows: List[RowElement[RowType]]
    _property_map: Mapping[str, UUID]
    _rev_property_map: Mapping[UUID, str]

    def __init__(self, asset_type_id: UUID, property_map: Mapping[str, UUID]):
        """
        The constructor for Table class.

        Parameters:
           asset_type_id (UUID): Id of the asset type corresponding with this table.
           property_map (Mapping[str, UUID]): Mapping of all field of row of this table to property ids.
        """

        self._asset_type_id = asset_type_id
        self._rows = []
        self._property_map = property_map
        self._rev_property_map = {v: k for k, v in property_map.items()}

    def __get_row_type(self):
        # __orig_class__ is an implementation detail but the benefits are too enticing
        return get_args(self.__orig_class__)[0]  # type: ignore

    def __len__(self):
        return len(self._rows)

    def __getitem__(self, key: int):
        return self._rows[key].row

    def __set__item__(self, key: int, value: RowType):
        if not isinstance(value, self.__get_row_type()):
            raise TypeError
        self._rows[key].row = value

    def __delitem__(self, key: int):
        del self._rows[key]

    def __iter__(self) -> Generator[RowType, None, None]:
        return (rowElem.row for rowElem in self._rows)

    def __reversed__(self) -> Generator[RowType, None, None]:
        return (rowElem.row for rowElem in reversed(self._rows))

    def appendRow(self, value: RowType):
        """ Adds the row to the end of the table. Returns a row reference. """
        if not isinstance(value, self.__get_row_type()):
            raise TypeError

        asset_id = uuid4()
        self._rows.append(RowElement[RowType](value, asset_id))
        return RowReference[RowType](self._asset_type_id, asset_id)

    def getReferenceByRowIndex(self, rowIndex: int):
        """ Get a reference to the specified row """
        asset_id = self._rows[rowIndex].asset_id
        return RowReference[RowType](self._asset_type_id, asset_id)

    def load(self):
        reply = self.__stub.readTable(ReadTableRequest(
            inspectionId="b2f3b819-c172-45bb-add1-1f004bb6b561", assetTypeId=str(self._asset_type_id)
        ))
        for row in reply.rows:
            localRow = self.__get_row_type()()

            for field in row.fields:
                attributeName = self._rev_property_map.get(
                    UUID(field.propertyId))
                if (attributeName is None):
                    logging.warning(
                        'Field with property id %s not found', field.propertyId)
                    continue
                match field.WhichOneof("value"):
                    case "numbers" if field.multi:
                        setattr(localRow, attributeName,
                                field.numbers.elements)
                    case "numbers":
                        value = next(iter(field.numbers.elements), None)
                        setattr(localRow, attributeName, value)
                    case "strings" if field.multi:
                        setattr(localRow, attributeName,
                                field.strings.elements)
                    case "strings":
                        value = next(iter(field.strings.elements), None)
                        setattr(localRow, attributeName, value)
                    case "members":
                        enumType = type(getattr(localRow, attributeName))
                        flagValue = reduce(lambda r, m: r | 2**(m-1),
                                           field.members.elements, 0)
                        setattr(localRow, attributeName, enumType(flagValue))
            self._rows.append(RowElement(localRow, row.assetId))


FieldType = TypeVar('FieldType')


class ImageField:
    """ This class allows saving and reading images in fields """
    _property_id: UUID

    def __init__(self, property_id: UUID):
        """
        The constructor for the ImageField class.

        Parameters:
           property_id (UUID): Id of the image property corresponding to this field
        """
        self._property_id = property_id

    def loadImage(self) -> Optional[BufferedIOBase]:
        """ Loads an image and returns it as a binary stream if present """
        pass

    def saveImage(self, image: BufferedIOBase):
        """ Writes the given binary stream as the image of this field  """
        pass
