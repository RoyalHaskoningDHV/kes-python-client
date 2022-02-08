from dataclasses import dataclass
from io import BufferedIOBase
from typing import List, Generic, Mapping, Optional, TypeVar, get_args
from uuid import UUID, uuid4

RowType = TypeVar('RowType')


@dataclass
class RowElement(Generic[RowType]):
    row: RowType
    assetId: UUID


class Table(Generic[RowType]):
    _assetTypeId: UUID
    _rows: List[RowElement[RowType]]
    _property_map: Mapping[str, UUID]

    def __init__(self, assetTypeId: UUID, property_map: Mapping[str, UUID]):
        self._assetTypeId = assetTypeId
        self._rows = []
        self._property_map = property_map

    def get_row_type(self):
        # __orig_class__ is an implementation detail but the benefits are too enticing
        return get_args(self.__orig_class__)[0]  # type: ignore

    def __len__(self):
        return len(self._rows)

    def __getitem__(self, key: int):
        return self._rows[key].row

    def __set__item__(self, key: int, value: RowType):
        if not isinstance(value, self.get_row_type()):
            raise TypeError
        self._rows[key].row = value

    def __delitem__(self, key: int):
        del self._rows[key]

    def __iter__(self):
        return (rowElem.row for rowElem in self._rows)

    def __reverse__(self):
        return(self._rows[i].row for i in range(len(self), -1, -1))

    def appendRow(self, value: RowType):
        if not isinstance(value, self.get_row_type()):
            raise TypeError
        self._rows.append(RowElement[RowType](value, uuid4()))


FieldType = TypeVar('FieldType')


class ImageField:
    def loadImage(self) -> Optional[BufferedIOBase]:
        pass

    def saveImage(self, image: BufferedIOBase):
        pass
