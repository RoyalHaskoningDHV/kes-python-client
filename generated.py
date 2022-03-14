from dataclasses import dataclass, field
from enum import Flag, auto
from typing import Container, Optional
from uuid import UUID
from kes import ImageField, LocationField, RowReference, Table


@dataclass
class TestCategoryTestAssetRow:
    _image_property: ImageField = field(default_factory=lambda: ImageField(
        UUID("dac71806-0c7d-4048-8328-df1678bdac7d")), init=False)

    @property
    def image_property(self):
        return self._image_property

    string_test_property: Optional[str] = None
    decimal_test_property: Optional[float] = None
    _location_property: LocationField = field(default_factory=lambda: LocationField(
        UUID("11dcdad3-8883-4849-859e-21af94eca03e")), init=False)

    @property
    def location_property(self):
        return self._location_property



test_category_test_asset_row_property_map = {
    "image_property": UUID("dac71806-0c7d-4048-8328-df1678bdac7d"),
    "string_test_property": UUID("ac0c9375-f925-49a3-94b5-4331249c9fc2"),
    "decimal_test_property": UUID("3ef0add5-81dc-4f5f-a85b-2a4792e5075a"),
    "location_property": UUID("11dcdad3-8883-4849-859e-21af94eca03e")
}

test_category_test_asset_table = Table[TestCategoryTestAssetRow](
    UUID("8f13751f-d671-4516-bae4-bd49a59719f2"), test_category_test_asset_row_property_map
)
