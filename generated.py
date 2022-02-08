from dataclasses import dataclass
from enum import Flag, auto
from typing import Container, Optional
from uuid import UUID
from meta import ImageField, Table


class Expertise(Flag):
    BACKEND = auto()
    FRONTEND = auto()
    DEVOPS = auto()


@dataclass
class ProgrammerRow:
    name: Optional[str]				        # Text property
    aliases: Container[str]		            # Repeating text property
    age: Optional[float]                    # Number field
    expertise: Optional[Expertise]			# single or multiple choice
    mug_shot: ImageField                    # Image property, snake-cased.


row_property_map = {
    "name": UUID("name-property-id"),
    "aliases": UUID("aliases_property-id"),
    "age": UUID("age-property-id"),
    "expertise": UUID("expertise-property-id"),
    "mug_shot": UUID("mug-shot-property-id")
}


progammerTable = Table[ProgrammerRow](
    UUID("programmer_asset_type_id"), row_property_map)
