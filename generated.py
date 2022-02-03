from enum import Flag, auto
from meta import ListOfStringFields, NumberField, StringField


class Expertise(Flag):
    BACKEND = auto()		# Is auto smart here?
    FRONTEND = auto()
    DEVOPS = auto()


class ProgrammerRow:
    name: StringField				# Text property
    aliases: ListOfStringFields		# Repeating text propertny
    age: NumberField
    expertise: Expertise			# single or multiple choice
