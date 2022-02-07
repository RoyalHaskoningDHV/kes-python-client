from dataclasses import dataclass
from io import BufferedIOBase
from typing import List, Generic, Optional, TypeVar, get_args

RowType = TypeVar('RowType')


@dataclass
class RowElement(Generic[RowType]):
    row: RowType
    assetId: Optional[str]


class Table(Generic[RowType]):
    _assetTypeId: str
    _rows: List[RowElement[RowType]]

    def __init__(self, assetTypeId: str):
        self._assetTypeId = assetTypeId
        self._rows = []

    def get_row_type(self):
        # __orig_class__ is an implementation detail but the benefits are too enticing
        return get_args(self.__orig_class__)[0]  # type: ignore

    def __len__(self):
        return len(self._rows)

    def __getitem__(self, key):
        return self._rows[key].row

    def __set__item__(self, key, value: RowType):
        if not isinstance(value, self.get_row_type()):
            raise TypeError
        self._rows[key].row = value

    def __delitem__(self, key):
        del self._rows[key]

    def __iter__(self):
        return (rowElem.row for rowElem in self._rows)

    def __reverse__(self):
        return reversed(iter(self))

    def appendRow(self, value: RowType):
        if not isinstance(value, self.get_row_type()):
            raise TypeError
        self._rows.append(RowElement[RowType](value, None))


FieldType = TypeVar('FieldType')


class ScalarField(Generic[FieldType]):
    _property_id: str
    _value: Optional[FieldType]

    def __init__(self, property_id: str):
        self._property_id = property_id
        self._value = None

    @property
    def value(self):
        return self._value

    def get_field_type(self):
        # __orig_class__ is an implementation detail but the benefits are too enticing
        return get_args(self.__orig_class__)[0]  # type: ignore

    @value.setter
    def value(self, newValue: FieldType):
        if not isinstance(newValue, self.get_field_type()):
            raise TypeError
        self._value = newValue

    @value.deleter
    def value(self):
        self._value = None


class ListField(Generic[FieldType]):
    _property_id: str
    _value: List[FieldType]

    def get_field_type(self):
        # __orig_class__ is an implementation detail but the benefits are too enticing
        return get_args(self.__orig_class__)[0]  # type: ignore

    def __init__(self, property_id: str):
        self._property_id = property_id
        self._value = []

    def __len__(self):
        return len(self._value)

    def __getitem__(self, key):
        return self._value[key]

    def __set__item__(self, key, value: FieldType):
        if not isinstance(value, self.get_field_type()):
            raise TypeError
        self._value[key] = value

    def __delitem__(self, key):
        del self._value[key]

    def __iter__(self):
        return iter(self._value)

    def __reverse__(self):
        return reversed(self._value)

    def appendValue(self, value: FieldType):
        if not isinstance(value, self.get_field_type()):
            raise TypeError
        self._value.append(value)

    def insertValue(self, index, value: FieldType):
        if not isinstance(value, self.get_field_type()):
            raise TypeError
        self._value.insert(index, value)

    def clear(self):
        self._value.clear()


class ImageField:
    _property_id: str

    def loadImage(self) -> BufferedIOBase:
        pass

    def saveImage(self, image: BufferedIOBase):
        pass


StringField = ScalarField[str]
NumberField = ScalarField[float]
ListOfStringsField = ListField[str]
ListOfNumbersField = ListField[float]

Enum = TypeVar("Enum")
EnumField = ScalarField[Enum]
