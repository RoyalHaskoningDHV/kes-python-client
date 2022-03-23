from dataclasses import dataclass
from typing import Iterator, List
from uuid import UUID


class LocationField:
    """ This class allows saving and reading location in fields """

    @dataclass
    class Point:
        name: str
        latitude: float
        longitude: float
        address: str

    _property_id: UUID
    _points: List[Point]

    def __init__(self, property_id: UUID):
        self._property_id = property_id
        self._points = []

    def addLocation(self, name: str, latitude: float, longitude: float, address: str):
        location = self.Point(name=name, latitude=latitude, longitude=longitude, address=address)
        self._points.append(location)

    def getPoints(self):
        return self._points

    def __getitem__(self, key: int):
        return self._points[key]

    def __set__item__(self, key: int, value: Point):
        self._points[key] = value

    def __len__(self):
        return len(self._points)

    def __iter__(self) -> Iterator[Point]:
        return iter(self._points)

    def __reversed__(self) -> Iterator[Point]:
        return reversed(self._points)

    def append(self, value: Point):
        self._points.append(value)