from dataclasses import dataclass
from enum import Flag, auto
from typing import Optional
from uuid import UUID

from kes import Table


class Expertise(Flag):
    Choice1 = auto()
    Choice3 = auto()
    Choice0 = auto()
    Choice2 = auto()


@dataclass
class TestAssetRow:
    text: Optional[str] = None
    number: Optional[float] = None
    enumeration: Optional[Expertise] = Expertise(0)


test_row_property_map = {
    "text": UUID("d706c793-7be2-4dcd-a63c-b83b26088dd0"),
    "number": UUID("e47cbe1c-2228-44b6-8a56-1250b67cf06c"),
    "enumeration": UUID("747bf852-95ff-4178-9397-bfbcf5ed951c")
}

TestAssetTable = Table[TestAssetRow](
    UUID("61521f07-beea-44fe-874c-31605a4313d4"), test_row_property_map
)


# DEMO
TestAssetTable.load()
print("text: ", TestAssetTable[0].text)
print("number: ", TestAssetTable[0].number)
print("enumeration", TestAssetTable[0].enumeration)

del TestAssetTable[0]

testAsset = TestAssetRow(text="Roel", number=666.0,
                         enumeration=Expertise.Choice1 | Expertise.Choice2)

TestAssetTable.appendRow(testAsset)
