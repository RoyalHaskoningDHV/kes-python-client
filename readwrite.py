from dataclasses import dataclass
from enum import Flag, auto
from uuid import UUID

from kes import Table


class Expertise(Flag):
    Choice1 = auto()
    Choice2 = auto()
    Choice3 = auto()
    Choice4 = auto()


@dataclass
class TestAssetRow:
    text = None
    number = None
    enumeration = Expertise(0)


test_row_property_map = {
    "text": UUID("d706c793-7be2-4dcd-a63c-b83b26088dd0"),
    "number": UUID("e47cbe1c-2228-44b6-8a56-1250b67cf06c"),
    "enumeration": UUID("747bf852-95ff-4178-9397-bfbcf5ed951c")
}

TestAssetTable = Table[TestAssetRow](
    UUID("61521f07-beea-44fe-874c-31605a4313d4"), test_row_property_map
)

TestAssetTable.load()

print(TestAssetTable._rows)
