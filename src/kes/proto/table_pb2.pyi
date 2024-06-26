"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.message
import google.protobuf.timestamp_pb2
import typing
import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

class ReadTableRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    ACTIVITYID_FIELD_NUMBER: builtins.int
    TABLEID_FIELD_NUMBER: builtins.int
    activityId: typing.Text
    tableId: typing.Text
    def __init__(self,
        *,
        activityId: typing.Text = ...,
        tableId: typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["activityId",b"activityId","tableId",b"tableId"]) -> None: ...
global___ReadTableRequest = ReadTableRequest

class AddRowsRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    ACTIVITYID_FIELD_NUMBER: builtins.int
    TABLEID_FIELD_NUMBER: builtins.int
    ROWS_FIELD_NUMBER: builtins.int
    activityId: typing.Text
    tableId: typing.Text
    @property
    def rows(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___Row]: ...
    def __init__(self,
        *,
        activityId: typing.Text = ...,
        tableId: typing.Text = ...,
        rows: typing.Optional[typing.Iterable[global___Row]] = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["activityId",b"activityId","rows",b"rows","tableId",b"tableId"]) -> None: ...
global___AddRowsRequest = AddRowsRequest

class DeleteAllRowsRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    ACTIVITYID_FIELD_NUMBER: builtins.int
    TABLEID_FIELD_NUMBER: builtins.int
    activityId: typing.Text
    tableId: typing.Text
    def __init__(self,
        *,
        activityId: typing.Text = ...,
        tableId: typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["activityId",b"activityId","tableId",b"tableId"]) -> None: ...
global___DeleteAllRowsRequest = DeleteAllRowsRequest

class DeleteRowsRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    ACTIVITYID_FIELD_NUMBER: builtins.int
    ROWIDS_FIELD_NUMBER: builtins.int
    activityId: typing.Text
    @property
    def rowIds(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[typing.Text]: ...
    def __init__(self,
        *,
        activityId: typing.Text = ...,
        rowIds: typing.Optional[typing.Iterable[typing.Text]] = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["activityId",b"activityId","rowIds",b"rowIds"]) -> None: ...
global___DeleteRowsRequest = DeleteRowsRequest

class Rows(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    ROWS_FIELD_NUMBER: builtins.int
    @property
    def rows(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___Row]: ...
    def __init__(self,
        *,
        rows: typing.Optional[typing.Iterable[global___Row]] = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["rows",b"rows"]) -> None: ...
global___Rows = Rows

class Row(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    ASSETID_FIELD_NUMBER: builtins.int
    FIELDS_FIELD_NUMBER: builtins.int
    assetId: typing.Text
    @property
    def fields(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___Field]: ...
    def __init__(self,
        *,
        assetId: typing.Text = ...,
        fields: typing.Optional[typing.Iterable[global___Field]] = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["assetId",b"assetId","fields",b"fields"]) -> None: ...
global___Row = Row

class Field(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    PROPERTYID_FIELD_NUMBER: builtins.int
    MULTI_FIELD_NUMBER: builtins.int
    NUMBERS_FIELD_NUMBER: builtins.int
    STRINGS_FIELD_NUMBER: builtins.int
    MEMBERS_FIELD_NUMBER: builtins.int
    ROWREFERENCES_FIELD_NUMBER: builtins.int
    IMAGE_FIELD_NUMBER: builtins.int
    LOCATIONS_FIELD_NUMBER: builtins.int
    DATE_FIELD_NUMBER: builtins.int
    propertyId: typing.Text
    multi: builtins.bool
    @property
    def numbers(self) -> global___NumberValues: ...
    @property
    def strings(self) -> global___StringValues: ...
    @property
    def members(self) -> global___EnumerationValues: ...
    @property
    def rowReferences(self) -> global___RelationshipValues: ...
    @property
    def image(self) -> global___ImageValue: ...
    @property
    def locations(self) -> global___LocationValues: ...
    @property
    def date(self) -> google.protobuf.timestamp_pb2.Timestamp: ...
    def __init__(self,
        *,
        propertyId: typing.Text = ...,
        multi: builtins.bool = ...,
        numbers: typing.Optional[global___NumberValues] = ...,
        strings: typing.Optional[global___StringValues] = ...,
        members: typing.Optional[global___EnumerationValues] = ...,
        rowReferences: typing.Optional[global___RelationshipValues] = ...,
        image: typing.Optional[global___ImageValue] = ...,
        locations: typing.Optional[global___LocationValues] = ...,
        date: typing.Optional[google.protobuf.timestamp_pb2.Timestamp] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["date",b"date","image",b"image","locations",b"locations","members",b"members","numbers",b"numbers","rowReferences",b"rowReferences","strings",b"strings","value",b"value"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["date",b"date","image",b"image","locations",b"locations","members",b"members","multi",b"multi","numbers",b"numbers","propertyId",b"propertyId","rowReferences",b"rowReferences","strings",b"strings","value",b"value"]) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions.Literal["value",b"value"]) -> typing.Optional[typing_extensions.Literal["numbers","strings","members","rowReferences","image","locations","date"]]: ...
global___Field = Field

class NumberValues(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    ELEMENTS_FIELD_NUMBER: builtins.int
    @property
    def elements(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.float]: ...
    def __init__(self,
        *,
        elements: typing.Optional[typing.Iterable[builtins.float]] = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["elements",b"elements"]) -> None: ...
global___NumberValues = NumberValues

class StringValues(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    ELEMENTS_FIELD_NUMBER: builtins.int
    @property
    def elements(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[typing.Text]: ...
    def __init__(self,
        *,
        elements: typing.Optional[typing.Iterable[typing.Text]] = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["elements",b"elements"]) -> None: ...
global___StringValues = StringValues

class EnumerationValues(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    ELEMENTS_FIELD_NUMBER: builtins.int
    @property
    def elements(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.int]: ...
    def __init__(self,
        *,
        elements: typing.Optional[typing.Iterable[builtins.int]] = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["elements",b"elements"]) -> None: ...
global___EnumerationValues = EnumerationValues

class RelationshipValues(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    ELEMENTS_FIELD_NUMBER: builtins.int
    @property
    def elements(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[typing.Text]: ...
    def __init__(self,
        *,
        elements: typing.Optional[typing.Iterable[typing.Text]] = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["elements",b"elements"]) -> None: ...
global___RelationshipValues = RelationshipValues

class ImageValue(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    ID_FIELD_NUMBER: builtins.int
    FILENAME_FIELD_NUMBER: builtins.int
    TEMPKEY_FIELD_NUMBER: builtins.int
    id: typing.Text
    fileName: typing.Text
    tempKey: typing.Text
    def __init__(self,
        *,
        id: typing.Text = ...,
        fileName: typing.Text = ...,
        tempKey: typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["fileName",b"fileName","id",b"id","tempKey",b"tempKey"]) -> None: ...
global___ImageValue = ImageValue

class LocationValues(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    ELEMENTS_FIELD_NUMBER: builtins.int
    @property
    def elements(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___LocationPoint]: ...
    def __init__(self,
        *,
        elements: typing.Optional[typing.Iterable[global___LocationPoint]] = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["elements",b"elements"]) -> None: ...
global___LocationValues = LocationValues

class LocationPoint(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    NAME_FIELD_NUMBER: builtins.int
    LATITUDE_FIELD_NUMBER: builtins.int
    LONGITUDE_FIELD_NUMBER: builtins.int
    ADDRESS_FIELD_NUMBER: builtins.int
    name: typing.Text
    latitude: builtins.float
    longitude: builtins.float
    address: typing.Text
    def __init__(self,
        *,
        name: typing.Text = ...,
        latitude: builtins.float = ...,
        longitude: builtins.float = ...,
        address: typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["address",b"address","latitude",b"latitude","longitude",b"longitude","name",b"name"]) -> None: ...
global___LocationPoint = LocationPoint

class LoadImageRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    IMAGEVALUEID_FIELD_NUMBER: builtins.int
    FILENAME_FIELD_NUMBER: builtins.int
    imageValueId: typing.Text
    fileName: typing.Text
    def __init__(self,
        *,
        imageValueId: typing.Text = ...,
        fileName: typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["fileName",b"fileName","imageValueId",b"imageValueId"]) -> None: ...
global___LoadImageRequest = LoadImageRequest

class LoadImageReply(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    CHUNK_FIELD_NUMBER: builtins.int
    chunk: builtins.bytes
    def __init__(self,
        *,
        chunk: builtins.bytes = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["chunk",b"chunk"]) -> None: ...
global___LoadImageReply = LoadImageReply

class SaveImageRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    CHUNK_FIELD_NUMBER: builtins.int
    chunk: builtins.bytes
    def __init__(self,
        *,
        chunk: builtins.bytes = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["chunk",b"chunk"]) -> None: ...
global___SaveImageRequest = SaveImageRequest

class SaveImageReply(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    TEMPKEY_FIELD_NUMBER: builtins.int
    tempKey: typing.Text
    def __init__(self,
        *,
        tempKey: typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["tempKey",b"tempKey"]) -> None: ...
global___SaveImageReply = SaveImageReply
