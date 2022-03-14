"""This module offers client functionality for accessing assets and properties through the abstraction provided by the table class.

Classes:
    Table: Rows represent assets and columns properties.
"""
import logging
import uuid
from dataclasses import dataclass
from enum import Flag
from functools import reduce
from io import BufferedIOBase
import logging
from typing import Generator, List, Generic, Mapping, Optional, Type, TypeVar
from uuid import UUID, uuid4

import grpc

from table_pb2 import AddRowsRequest, DeleteRowsRequest, ReadTableRequest, TableReply, LoadImageRequest, LocationPoint, \
    SaveImageRequest, SaveImageReply
from table_pb2_grpc import *

from proto.table_pb2 import AddRowsRequest, DeleteRowsRequest, ReadTableRequest, TableReply
from proto.table_pb2_grpc import TableStub

RowType = TypeVar('RowType')
chunkSize = 60 * 1024  # 64 KiB


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
            field = row.fields.add()
            field.propertyId = str(propertyId)
            match getattr(value, fieldName):
                case float(floatValue):
                    field.numbers.elements.append(floatValue)
                case str(textValue):
                    field.strings.elements.append(textValue)
                case ImageField() as imageValue:
                    field.image.fileName = imageValue.name
                    field.image.tempKey = imageValue._temp_key
                case LocationField() as locationValue:
                    for point in locationValue._points:
                        locPoint = LocationPoint(name=point.name, latitude=point.latitude,
                                                 longitude=point.longitude, address=point.address)
                        field.locations.elements.append(locPoint)
                case [firstNumber, *rest] if isinstance(firstNumber, float):
                    field.numbers.elements[:] = [firstNumber, *rest]
                case [firstString, *rest] if type(firstString) == str:
                    field.strings.elements[:] = [firstString, *rest]
                case Flag() as flag:
                    for i, c in enumerate(bin(flag.value)[:1:-1], 1):
                        if c == '1':
                            field.members.elements.append(i)
                case _:
                    pass

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
                    case "image":
                        imageField = ImageField(property_id=field.propertyId)
                        imageField.name = field.image.fileName
                        imageField._image_value_id = field.image.id
                        setattr(localRow, "_" + attributeName, imageField)
                    case "locations":
                        locationField = LocationField(property_id=field.propertyId)
                        for point in field.locations.elements:
                            locationField.addLocation(point.name, point.latitude, point.longitude, point.address)
                        setattr(localRow, "_" + attributeName, locationField)
                    case "members":
                        enumType = type(getattr(localRow, attributeName))
                        flagValue = reduce(lambda r, m: r | 2**(m - 1),
                                           field.members.elements, 0)
                        setattr(localRow, attributeName, enumType(flagValue))
                    case _:
                        pass
            self._rows.append(RowElement[RowType](
                localRow, uuid.UUID(row.assetId)))


@dataclass
class TableDef(Generic[RowType]):
    row_type: Type[RowType]
    asset_type_id: UUID
    property_map: Mapping[str, UUID]


class ImageField:
    """ This class allows saving and reading images in fields """
    _property_id: UUID
    _image_value_id: UUID
    file: bytes
    name: str
    _temp_key: str

    def __init__(self, property_id: UUID):
        """
        The constructor for the ImageField class.

        Parameters:
           property_id (UUID): Id of the image property corresponding to this field
        """
        self._property_id = property_id
        self._image_value_id = None
        self.name = ""
        self.file = None
        self._temp_key = None

    def loadImage(self):
        """ Loads an image and returns it as a binary stream if present """
        chunks = []
        streamingReply = stub.loadImage(LoadImageRequest(
            imageValueId=str(self._image_value_id), fileName=self.name
        ))
        for reply in streamingReply:
            chunks.append(reply.chunk)

        self.file = b''.join(chunks)
        return self.file

    def saveImage(self, name: str, image: bytes):
        """ Writes the given binary stream as the image of this field  """
        self.file = image
        self.name = name
        response: SaveImageReply = stub.saveImage(createChunkStreams(image))
        self._temp_key = response.tempKey


def createChunkStreams(image: bytes):
    for i in range(0, len(image), chunkSize):
        yield SaveImageRequest(chunk=image[i:i + chunkSize])


class LocationField:
    """ This class allows saving and reading location in fields """

    @dataclass
    class Point:
        name: str
        latitude: float
        longitude: float
        address: str

    _property_id: UUID
    _points: List[Point]

    def __init__(self, property_id: UUID):
        self._property_id = property_id
        self._points = []

    def addLocation(self, name: str, latitude: float, longitude: float, address: str):
        location = self.Point(name=name, latitude=latitude, longitude=longitude, address=address)
        self._points.append(location)

    def getPoints(self):
        return self._points

    def __getitem__(self, key: int):
        return self._points[key]

    def append(self, value: Point):
        self._points.append(value)
