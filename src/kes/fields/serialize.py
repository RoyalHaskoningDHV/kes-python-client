from enum import Flag
from functools import reduce
from typing import Any
from uuid import UUID
from kes.fields.imagefield import ImageField
from kes.fields.locationfield import LocationField
from kes.proto.table_pb2 import LocationPoint, Field as pb_Field


def serializeField(pb_field: pb_Field, property_id: UUID, field: Any):
    pb_field.propertyId = str(property_id)
    match field:
        case float(floatValue):
            pb_field.numbers.elements.append(floatValue)
        case str(textValue):
            pb_field.strings.elements.append(textValue)
        case ImageField() as imageValue:
            if imageValue.key != None:
                pb_field.image.fileName = imageValue.name
                pb_field.image.tempKey = imageValue.key
        case LocationField() as locationValue:
            for point in locationValue:
                locPoint = LocationPoint(name=point.name, latitude=point.latitude,
                                         longitude=point.longitude, address=point.address)
                pb_field.locations.elements.append(locPoint)
        case [firstNumber, *rest] if isinstance(firstNumber, float):
            pb_field.numbers.elements[:] = [firstNumber, *rest]
        case [firstString, *rest] if type(firstString) == str:
            pb_field.strings.elements[:] = [firstString, *rest]
        case Flag() as flag:
            for i, c in enumerate(bin(flag.value)[:1:-1], 1):
                if c == '1':
                    pb_field.members.elements.append(i)
        case _:
            pass


def deserializeField(row: Any, attribute_name: str, pb_field: pb_Field):
    match pb_field.WhichOneof("value"):
        case "numbers" if pb_field.multi:
            setattr(row, attribute_name,
                    pb_field.numbers.elements)
        case "numbers":
            value = next(iter(pb_field.numbers.elements), None)
            setattr(row, attribute_name, value)
        case "strings" if pb_field.multi:
            setattr(row, attribute_name,
                    pb_field.strings.elements)
        case "strings":
            value = next(iter(pb_field.strings.elements), None)
            setattr(row, attribute_name, value)
        case "image":
            imageRef = ImageField.ImageRef(pb_field.image.fileName, UUID(pb_field.image.id))
            imageField = ImageField(property_id=UUID(pb_field.propertyId), imageRef=imageRef)
            setattr(row, "_" + attribute_name, imageField)
        case "locations":
            locationField = LocationField(property_id=UUID(pb_field.propertyId))
            for point in pb_field.locations.elements:
                locationField.addLocation(point.name, point.latitude, point.longitude, point.address)
            setattr(row, "_" + attribute_name, locationField)
        case "members":
            enumType = type(getattr(row, attribute_name))
            flagValue = reduce(lambda r, m: r | 2**(m - 1),
                               pb_field.members.elements, 0)
            setattr(row, attribute_name, enumType(flagValue))
        case _:
            pass
