# THIS IS A GENERATED FILE. DO NOT EDIT.

from dataclasses import dataclass, field
from enum import Flag, auto
from typing import Optional
from uuid import UUID
from kes.table import TableDef, RowReference, FieldDef
from kes.fields.imagefield import ImageField
from kes.fields.locationfield import LocationField


class Singleselect(Flag):
    C = auto()
    B = auto()
    A = auto()


class Multipleselect(Flag):
    F = auto()
    E = auto()
    D = auto()


@dataclass
class CategoryAssetRow:
    singleselect: Optional[Singleselect] = None
    _image: ImageField = field(default_factory=lambda: ImageField(
        UUID("10f11f64-cdce-4ca7-9266-8afeb3a87f6c")), init=False)

    @property
    def image(self):
        return self._image

    _location: LocationField = field(default_factory=lambda: LocationField(
        UUID("39a81418-d542-46d5-959b-924a51c4885b")), init=False)

    @property
    def location(self):
        return self._location

    text: Optional[str] = None
    amount: Optional[float] = None
    multipleselect: Optional[Multipleselect] = None


category_asset_table_def = TableDef[CategoryAssetRow](
    row_type=CategoryAssetRow,
    asset_type_id=UUID("c1b19055-71bb-4355-ab79-426841ca58f3"),
    property_map={
        "singleselect": FieldDef(UUID("d0165c6c-3a53-4126-b701-44cab335853a"), Singleselect),
        "image": FieldDef(UUID("10f11f64-cdce-4ca7-9266-8afeb3a87f6c"), None),
        "location": FieldDef(UUID("39a81418-d542-46d5-959b-924a51c4885b"), None),
        "text": FieldDef(UUID("da1df664-e1ae-4b00-aef5-8e5d86ec74da"), None),
        "amount": FieldDef(UUID("f03d4f5f-a76c-4f20-ab89-5e452b437627"), None),
        "multipleselect": FieldDef(UUID("7cfdbda8-02e3-47b5-9dae-aa8246baf5d3"), Multipleselect)
    }
)


@dataclass
class CategoryParentAssetRow:
    relationship: Optional[RowReference[CategoryAssetRow]] = None


category_parent_asset_table_def = TableDef[CategoryParentAssetRow](
    row_type=CategoryParentAssetRow,
    asset_type_id=UUID("bd3ada3c-dc9c-4366-935a-963936faf391"),
    property_map={
        "relationship": FieldDef(UUID("3a977520-4d23-4de2-a0a9-71f5f795fd47"), None)
    }
)
