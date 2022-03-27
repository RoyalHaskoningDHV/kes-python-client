from dataclasses import dataclass
from typing import ByteString, Optional
from uuid import UUID

from kes.proto.table_pb2_grpc import TableStub
from kes.proto.table_pb2 import LoadImageRequest, SaveImageReply, SaveImageRequest


class ImageUndefined(Exception):
    ...


class ImageField:
    """ This class allows saving and reading images in fields """

    @dataclass
    class ImageRef:
        name: str
        value_id: UUID

    @dataclass
    class ImageUpload:
        name: str
        key: str

    _property_id: UUID
    _ref: ImageRef | ImageUpload | None
    __chunkSize = 60 * 1024  # 64 KiB

    def __init__(self, property_id: UUID, imageRef: Optional[ImageRef] = None):
        """
        The constructor for the ImageField class.

        Parameters:
           property_id (UUID): Id of the image property corresponding to this field
        """
        self._property_id = property_id
        self._ref = imageRef

    def load(self, stub: TableStub) -> ByteString:
        """ Loads an image and returns it as a binary stream if present """
        if not isinstance(self._ref, self.ImageRef):
            raise ImageUndefined

        imageData = bytearray()
        streamingReply = stub.loadImage(LoadImageRequest(
            imageValueId=str(self._ref.value_id), fileName=self._ref.name
        ))
        for reply in streamingReply:
            imageData += reply.chunk

        return imageData

    def save(self, stub: TableStub, name: str, data: bytes):
        """ Writes the given binary stream as the image of this field  """
        response: SaveImageReply = stub.saveImage(self._createChunkStreams(data))
        self._ref = self.ImageUpload(name, response.tempKey)

    def _createChunkStreams(self, image: bytes):
        for i in range(0, len(image), self.__chunkSize):
            chunk = image[i: i + self.__chunkSize]
            yield SaveImageRequest(chunk=chunk)

    def isEmpty(self) -> bool:
        return self._ref is None

    @property
    def name(self):
        if self._ref != None:
            return self._ref.name
        else:
            return ""

    @property
    def key(self):
        if isinstance(self._ref, self.ImageUpload):
            return self._ref.key
        else:
            return ""
