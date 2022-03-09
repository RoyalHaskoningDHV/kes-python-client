from dataclasses import dataclass, field
from enum import Flag, auto
from typing import Container, Optional
from uuid import UUID
from kes import ImageField, LocationField, RowReference, Table


@dataclass
class TestCategoryTestAssetRow:
    string_test_property: Optional[str] = None
    decimal_test_property: Optional[float] = None
    _image_property: ImageField = field(default_factory=lambda: ImageField(
        UUID("44e5526c-faac-44c2-9eb0-bff829cff556")), init=False)

    @property
    def image_property(self):
        return self._image_property

    _location_property: LocationField = field(default_factory=lambda: LocationField(
        UUID("0d98518d-97c7-4c38-b37d-2bf41264efd3")), init=False)

    @property
    def location_property(self):
        return self._location_property



test_category_test_asset_row_property_map = {
    "string_test_property": UUID("45fbf341-e574-4bb2-b334-e03823f44e9b"),
    "decimal_test_property": UUID("320e84e5-b200-4c02-b8ed-df61d7438de0"),
    "image_property": UUID("44e5526c-faac-44c2-9eb0-bff829cff556"),
    "location_property": UUID("0d98518d-97c7-4c38-b37d-2bf41264efd3")
}

test_category_test_asset_table = Table[TestCategoryTestAssetRow](
    UUID("8032e814-c705-4974-a3c1-e45622283e05"), test_category_test_asset_row_property_map
)
