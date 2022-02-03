from typing import Container, Generic, Optional, Sequence, TypeVar, get_args

RowType = TypeVar('RowType')


class Table(Generic[RowType]):
    __assetTypeId: str

    rows: Container[RowType]


FieldType = TypeVar('FieldType', str, float)


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


StringField = ScalarField[str]
NumberField = ScalarField[float]
ListOfStringFields = Sequence[StringField]
ListOfNumberFields = Sequence[NumberField]
