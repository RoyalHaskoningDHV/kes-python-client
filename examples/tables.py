# THIS IS A GENERATED FILE. DO NOT EDIT.

from dataclasses import dataclass, field
from enum import Flag, auto
from typing import Container, Optional
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
        UUID("51673021-9e75-4348-849c-e1280bb35fd5")), init=False)

    @property
    def image(self):
        return self._image

    multipleselect: Optional[Multipleselect] = None
    _location: LocationField = field(default_factory=lambda: LocationField(
        UUID("fc30d0f6-23c8-468b-a48e-b12796ee5bec")), init=False)

    @property
    def location(self):
        return self._location

    text: Optional[str] = None
    amount: Optional[float] = None


category_asset_table_def = TableDef[CategoryAssetRow](
    row_type=CategoryAssetRow,
    asset_type_id=UUID("d7707940-8c91-4231-bf44-fb07497575cc"),
    property_map={
        "singleselect": FieldDef(UUID("7b03cddb-4216-4de4-bc21-93d38014edea"), Singleselect),
        "image": FieldDef(UUID("51673021-9e75-4348-849c-e1280bb35fd5"), None),
        "multipleselect": FieldDef(UUID("9782b775-07b8-4da0-b18b-7558f62e4a11"), Multipleselect),
        "location": FieldDef(UUID("fc30d0f6-23c8-468b-a48e-b12796ee5bec"), None),
        "text": FieldDef(UUID("5278e509-d35b-4bc2-9825-ee5b58cf6cac"), None),
        "amount": FieldDef(UUID("823021a2-9741-4429-a5bc-fdb31f520d42"), None)
    }
)


@dataclass
class CategoryParentAssetRow:
    relationship: Optional[RowReference[CategoryAssetRow]] = None


category_parent_asset_table_def = TableDef[CategoryParentAssetRow](
    row_type=CategoryParentAssetRow,
    asset_type_id=UUID("94c5522f-5ecb-4eee-a5b8-637b0b946b50"),
    property_map={
        "relationship": FieldDef(UUID("b4aa7376-a029-41f4-9253-e822d783676f"), None)
    }
)
