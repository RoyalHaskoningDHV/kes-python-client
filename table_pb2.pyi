"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.message
import typing
import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

class ReadTableRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    INSPECTIONID_FIELD_NUMBER: builtins.int
    ASSETTYPEID_FIELD_NUMBER: builtins.int
    inspectionId: typing.Text
    assetTypeId: typing.Text
    def __init__(self,
        *,
        inspectionId: typing.Text = ...,
        assetTypeId: typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["assetTypeId",b"assetTypeId","inspectionId",b"inspectionId"]) -> None: ...
global___ReadTableRequest = ReadTableRequest

class AddRowsRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    INSPECTIONID_FIELD_NUMBER: builtins.int
    ASSETTYPEID_FIELD_NUMBER: builtins.int
    ROWS_FIELD_NUMBER: builtins.int
    inspectionId: typing.Text
    assetTypeId: typing.Text
    @property
    def rows(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___Row]: ...
    def __init__(self,
        *,
        inspectionId: typing.Text = ...,
        assetTypeId: typing.Text = ...,
        rows: typing.Optional[typing.Iterable[global___Row]] = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["assetTypeId",b"assetTypeId","inspectionId",b"inspectionId","rows",b"rows"]) -> None: ...
global___AddRowsRequest = AddRowsRequest

class DeleteRowsRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    INSPECTIONID_FIELD_NUMBER: builtins.int
    ASSETIDS_FIELD_NUMBER: builtins.int
    inspectionId: typing.Text
    @property
    def assetIds(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[typing.Text]: ...
    def __init__(self,
        *,
        inspectionId: typing.Text = ...,
        assetIds: typing.Optional[typing.Iterable[typing.Text]] = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["assetIds",b"assetIds","inspectionId",b"inspectionId"]) -> None: ...
global___DeleteRowsRequest = DeleteRowsRequest

class AddRowsReply(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    def __init__(self,
        ) -> None: ...
global___AddRowsReply = AddRowsReply

class DeleteRowsReply(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    def __init__(self,
        ) -> None: ...
global___DeleteRowsReply = DeleteRowsReply

class TableReply(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    ROWS_FIELD_NUMBER: builtins.int
    @property
    def rows(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___Row]: ...
    def __init__(self,
        *,
        rows: typing.Optional[typing.Iterable[global___Row]] = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["rows",b"rows"]) -> None: ...
global___TableReply = TableReply

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
    def image(self) -> global___ImageValue:
        """ImageValues images = 7"""
        pass
    @property
    def locations(self) -> global___LocationValues: ...
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
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["image",b"image","locations",b"locations","members",b"members","numbers",b"numbers","rowReferences",b"rowReferences","strings",b"strings","value",b"value"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["image",b"image","locations",b"locations","members",b"members","multi",b"multi","numbers",b"numbers","propertyId",b"propertyId","rowReferences",b"rowReferences","strings",b"strings","value",b"value"]) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions.Literal["value",b"value"]) -> typing.Optional[typing_extensions.Literal["numbers","strings","members","rowReferences","image","locations"]]: ...
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
    CHUNK_FIELD_NUMBER: builtins.int
    id: typing.Text
    fileName: typing.Text
    chunk: builtins.bytes
    def __init__(self,
        *,
        id: typing.Text = ...,
        fileName: typing.Text = ...,
        chunk: builtins.bytes = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["chunk",b"chunk","fileName",b"fileName","id",b"id"]) -> None: ...
global___ImageValue = ImageValue

class LocationValues(google.protobuf.message.Message):
    """message ImageValues {
     repeated Image elements = 1;
    }

    message Image {
     string fileName = 1;
     bytes chunk = 2;
    }

    """
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
