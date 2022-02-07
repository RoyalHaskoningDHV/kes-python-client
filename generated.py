from enum import Flag, auto
from meta import EnumField, ListOfStringsField, NumberField, StringField, Table


class Expertise(Flag):
    BACKEND = auto()
    FRONTEND = auto()
    DEVOPS = auto()


class ProgrammerRow:
    name: StringField				        # Text property
    aliases: ListOfStringsField		        # Repeating text propertny
    age: NumberField                        # Number field
    expertise: EnumField[Expertise]			# single or multiple choice


ProgammerTable = Table[ProgrammerRow]
