"""This module offers client functionality for accessing assets and properties through the abstraction provided by the table class.

Classes:
    Table: Rows represent assets and columns properties.
"""
from enum import Flag
from functools import reduce
import logging
import uuid
from dataclasses import dataclass
from typing import Any, Generator, List, Generic, Mapping, Type, TypeVar
from uuid import UUID, uuid4
from xmlrpc.client import Boolean
import grpc

from kes.fields.imagefield import ImageField

from kes.proto.table_pb2 import AddRowsRequest, DeleteRowsRequest, ReadTableRequest, TableReply, LocationPoint, Field as pb_Field
from kes.proto.table_pb2_grpc import TableStub

from kes.fields.locationfield import LocationField

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


@dataclass
class FieldDef:
    propertyId: UUID
    flag_constructor: Type[Flag] | None


PropertyMap = Mapping[str, FieldDef]


@dataclass
class TableDef(Generic[RowType]):
    row_type: Type[RowType]
    asset_type_id: UUID
    property_map: PropertyMap


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
    _property_map: PropertyMap
    _rev_property_map: Mapping[UUID, tuple[str, Type[Flag] | None]]

    def __init__(self, stub: TableStub, inspection_id: UUID, row_type: Type[RowType], asset_type_id: UUID, property_map: PropertyMap):
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
        self._rev_property_map = {v.propertyId: (k, v.flag_constructor) for k, v in property_map.items()}

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

        for fieldName, fieldDef in self._property_map.items():
            pb_field = row.fields.add()
            pb_field.propertyId = str(fieldDef.propertyId)
            field = getattr(value, fieldName)
            if self._fieldIsEmpty(field):
                continue
            self._serializeField(field, pb_field)
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
                revFieldDef = self._rev_property_map.get(UUID(field.propertyId))
                if (revFieldDef is None):
                    logging.warning(
                        'Field with property id %s not found', field.propertyId)
                    continue
                self._deserializeField(localRow, *revFieldDef, field)

            self._rows.append(RowElement[RowType](
                localRow, uuid.UUID(row.assetId)))

    def saveImage(self, image: ImageField, name: str, data: bytes):
        image.save(self._stub, name, data)

    def loadImage(self, image: ImageField):
        return image.load(self._stub)

    def _fieldIsEmpty(self, field: Any) -> bool:
        if self is None:
            return True

        if isinstance(field, ImageField):
            return field.isEmpty()

        return False

    def _serializeField(self, field: Any, pb_field: pb_Field):
        match field:
            case float(floatValue):
                pb_field.numbers.elements.append(floatValue)
            case str(textValue):
                pb_field.strings.elements.append(textValue)
            case ImageField() as imageValue:
                if imageValue.key != None:
                    pb_field.image.fileName = imageValue.name
                    pb_field.image.tempKey = imageValue.key
                else:
                    del pb_field
            case LocationField() as locationValue:
                for point in locationValue:
                    locPoint = LocationPoint(name=point.name, latitude=point.latitude,
                                             longitude=point.longitude, address=point.address)
                    pb_field.locations.elements.append(locPoint)
            case [firstNumber, *rest] if isinstance(firstNumber, float):
                pb_field.numbers.elements[:] = [firstNumber, *rest]
            case [firstString, *rest] if type(firstString) == str:
                pb_field.strings.elements[:] = [firstString, *rest]
            case Flag() as flag:
                for i, c in enumerate(bin(flag.value)[:1:-1], 1):
                    if c == '1':
                        pb_field.members.elements.append(i)
            case _:
                pass

    def _deserializeField(self, row: Any, attribute_name: str, flag_type: Type[Flag] | None, pb_field: pb_Field):
        match pb_field.WhichOneof("value"):
            case "numbers" if pb_field.multi:
                setattr(row, attribute_name,
                        pb_field.numbers.elements)
            case "numbers":
                value = next(iter(pb_field.numbers.elements), None)
                setattr(row, attribute_name, value)
            case "strings" if pb_field.multi:
                setattr(row, attribute_name,
                        pb_field.strings.elements)
            case "strings":
                value = next(iter(pb_field.strings.elements), None)
                setattr(row, attribute_name, value)
            case "image":
                imageRef = ImageField.ImageRef(pb_field.image.fileName, UUID(pb_field.image.id))
                imageField = ImageField(property_id=UUID(pb_field.propertyId), imageRef=imageRef)
                setattr(row, "_" + attribute_name, imageField)
            case "locations":
                locationField = LocationField(property_id=UUID(pb_field.propertyId))
                for point in pb_field.locations.elements:
                    locationField.addPoint(point.name, point.latitude, point.longitude, point.address)
                setattr(row, "_" + attribute_name, locationField)
            case "members":
                if flag_type is None:
                    raise LookupError("Flag type not set")
                flagValue = reduce(lambda r, m: r | 2**(m - 1),
                                   pb_field.members.elements, 0)
                setattr(row, attribute_name, flag_type(flagValue))
            case _:
                pass
