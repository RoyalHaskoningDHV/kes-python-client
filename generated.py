from dataclasses import dataclass
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
    name: Optional[str]


sweat_shop_row_property_map = {
    "name": UUID("sweat_shop_name_property_id")
}

sweat_shop_table = Table[SweatShopRow](
    UUID("sweat_shop_type_id"), sweat_shop_row_property_map
)


@dataclass
class ProgrammerRow:
    name: Optional[str]				        # Text property
    aliases: Container[str]		            # Repeating text property
    age: Optional[float]                    # Number field
    expertise: Optional[Expertise]			# single or multiple choice
    mug_shot: ImageField                    # Image property, snake_cased.
    sweat_shop: Optional[RowReference[SweatShopRow]]  # reference field


programmer_row_property_map = {
    "name": UUID("name_property_id"),
    "aliases": UUID("aliases_property_id"),
    "age": UUID("age_property_id"),
    "expertise": UUID("expertise_property_id"),
    "mug_shot": UUID("mug_shot_property_id")
}


progammer_table = Table[ProgrammerRow](
    UUID("programmer_asset_type_id"), programmer_row_property_map
)
