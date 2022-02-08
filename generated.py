from dataclasses import dataclass, field
from enum import Flag, auto
from typing import Container, Optional
from uuid import UUID
from meta import ImageField, RowReference, Table


class Expertise(Flag):
    BACKEND = auto()
    FRONTEND = auto()
    DEVOPS = auto()


# This must be defined BEFORE ProgrammerRow; rows without references should appear before rows with references
@dataclass
class SweatShopRow:
    name: Optional[str] = None


sweat_shop_row_property_map = {
    "name": UUID("a5638855-e5c9-4f15-8851-42add1689d18")
}

sweat_shop_table = Table[SweatShopRow](
    UUID("aaecc3be-99e2-43d0-9ef0-2a1f9b98f66c"), sweat_shop_row_property_map
)


@dataclass
class ProgrammerRow:
    # Compound Field: property id injected into constructor
    _mug_shot: ImageField = field(default_factory=lambda: ImageField(
        UUID("c6e25e1a-d182-404c-bd89-529808f51ee8")))

    name: Optional[str] = None
    # Repeating text property
    aliases: Container[str] = field(default_factory=list)
    age: Optional[float] = None
    expertise: Optional[Expertise] = None
    # reference field
    sweat_shop: Optional[RowReference[SweatShopRow]] = None

    @property
    def mug_shot(self):
        return self._mug_shot


programmer_row_property_map = {
    "name": UUID("31197f90-7392-4d53-8365-8e626508ecd9"),
    "aliases": UUID("3d1b7deb-8d44-4c4f-b303-08e39c14b0d5"),
    "age": UUID("eb1884b8-0d1e-4bd9-bd4a-87c17a57d4ed"),
    "expertise": UUID("4cbe5b83-34d1-4704-8830-d50e313217a5"),
    "mug_shot": UUID("c0c05d09-a61c-49ad-9adb-711851d65b86"),
    "sweat_shop": UUID("914a3bab-54d5-4609-9550-d5021fa9c7d7")
}


progammer_table = Table[ProgrammerRow](
    UUID("cf69ae6a-41ef-43cc-9b43-700d8269ccf8"), programmer_row_property_map
)
