from dataclasses import dataclass
from enum import Flag, auto
from meta import EnumField, ListOfStringsField, NumberField, StringField, Table


class Expertise(Flag):
    BACKEND = auto()
    FRONTEND = auto()
    DEVOPS = auto()


@dataclass
class ProgrammerRow:
    name: StringField				        # Text property
    aliases: ListOfStringsField		        # Repeating text propertny
    age: NumberField                        # Number field
    expertise: EnumField[Expertise]			# single or multiple choice


ProgrammerTable = Table[ProgrammerRow]
progammerTable = ProgrammerTable("programmer_asset_id")
