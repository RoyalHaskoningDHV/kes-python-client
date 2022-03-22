"""This module offers client functionality for accessing assets and properties through the abstraction provided by the table class.

Classes:
    Table: Rows represent assets and columns properties.
"""
import logging
import uuid
from dataclasses import dataclass
from typing import Generator, List, Generic, Mapping, Type, TypeVar
from uuid import UUID, uuid4

import grpc
from fields.imagefield import ImageField
from fields.serialize import deserializeField, serializeField

from proto.table_pb2 import AddRowsRequest, DeleteRowsRequest, ReadTableRequest, TableReply
from proto.table_pb2_grpc import TableStub

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


class TableFull(Exception):
    ...


class Table(Generic[RowType]):
    """
    This class acts as a container for rows.
    Each instance maps to a asset type, with rows corresponding to assets.

    Type parameters:
        RowType: The type of rows hold by this class.
    """

    _stub: TableStub
    _inspection_id: UUID
    _row_type: Type[RowType]
    _asset_type_id: UUID
    _rows: List[RowElement[RowType]]
    _property_map: Mapping[str, UUID]
    _rev_property_map: Mapping[UUID, str]

    def __init__(self, stub: TableStub, inspection_id: UUID, row_type: Type[RowType], asset_type_id: UUID, property_map: Mapping[str, UUID]):
        """
        The constructor for Table class.
        Tables are usually created using the :py:meth:Activity.build_table

        Parameters:
           inspection_id (UUID): Id of the inspection from which the table is read and written to.
           asset_type_id (UUID): Id of the asset type corresponding with this table.
           property_map (Mapping[str, UUID]): Mapping of all field of row of this table to property ids.
        """

        self._stub = stub
        self._inspection_id = inspection_id
        self._row_type = row_type
        self._asset_type_id = asset_type_id
        self._rows = []
        self._property_map = property_map
        self._rev_property_map = {v: k for k, v in property_map.items()}

    def __len__(self):
        return len(self._rows)

    def __getitem__(self, key: int):
        return self._rows[key].row

    def __set__item__(self, key: int, value: RowType):
        if not isinstance(value, self._row_type):
            raise TypeError
        self._rows[key].row = value

    def __delitem__(self, key: int):
        asset_id = self._rows[key].asset_id

        request = DeleteRowsRequest(assetIds=[str(asset_id)])
        self._stub.deleteRows(request)

        del self._rows[key]

    def __iter__(self) -> Generator[RowType, None, None]:
        return (rowElem.row for rowElem in self._rows)

    def __reversed__(self) -> Generator[RowType, None, None]:
        return (rowElem.row for rowElem in reversed(self._rows))

    def appendRow(self, value: RowType):
        """ Adds the row to the end of the table. Returns a row reference. """
        if not isinstance(value, self._row_type):
            raise TypeError

        request = AddRowsRequest()
        request.inspectionId = str(self._inspection_id)
        request.assetTypeId = str(self._asset_type_id)
        row = request.rows.add()
        asset_id = uuid4()
        row.assetId = str(asset_id)

        for fieldName, propertyId in self._property_map.items():
            pb_field = row.fields.add()
            field = getattr(value, fieldName)
            serializeField(pb_field, propertyId, field)
        try:
            self._stub.addRows(request)
        except grpc.RpcError as e:
            if e.code() == grpc.StatusCode.ALREADY_EXISTS:
                raise TableFull
            else:
                raise

        self._rows.append(RowElement[RowType](value, asset_id))
        return RowReference[RowType](self._asset_type_id, asset_id)

    def getReferenceByRowIndex(self, rowIndex: int):
        """ Get a reference to the specified row """
        asset_id = self._rows[rowIndex].asset_id
        return RowReference[RowType](self._asset_type_id, asset_id)

    def load(self):
        reply: TableReply = self._stub.readTable(ReadTableRequest(
            inspectionId=str(self._inspection_id), assetTypeId=str(self._asset_type_id)
        ))
        for row in reply.rows:
            localRow: RowType = self._row_type()

            for field in row.fields:
                attribute_name = self._rev_property_map.get(UUID(field.propertyId))
                if (attribute_name is None):
                    logging.warning(
                        'Field with property id %s not found', field.propertyId)
                    continue
                deserializeField(row, attribute_name, field)

            self._rows.append(RowElement[RowType](
                localRow, uuid.UUID(row.assetId)))

    def saveImage(self, image: ImageField, name: str, data: bytes):
        image.save(self._stub, name, data)

    def loadImage(self, image: ImageField):
        return image.load(self._stub)


@dataclass
class TableDef(Generic[RowType]):
    row_type: Type[RowType]
    asset_type_id: UUID
    property_map: Mapping[str, UUID]
