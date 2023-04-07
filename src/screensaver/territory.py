from typing import List

from src.screensaver.direction import Direction
from src.screensaver.flying_object import FlyingObject
from src.screensaver.position import Position


class Territory:
    def __init__(self, max_longitude: int = 100, max_latitude: int = 100):
        self.max_longitude = max_longitude
        self.min_longitude = 0
        self.max_latitude = max_latitude
        self.min_latitude = 0
        self.flying_objects = []

    def register(self, flying_object: FlyingObject):
        self.flying_objects.append(flying_object)
        # Proposal: handle the case of registering a collision

    def is_at_border(self, position: Position, direction: Direction) -> bool:
        directions = {
            direction.North: self._at_northern_border(position),
            direction.South: self._at_southern_border(position),
            direction.East: self._at_eastern_border(position),
            direction.West: self._at_western_border(position),
            direction.NorthEast: (
                self._at_northern_border(position) and self._at_eastern_border(position)
            ),
            direction.NorthWest: (
                self._at_northern_border(position) and self._at_western_border(position)
            ),
            direction.SouthEast: (
                self._at_southern_border(position) and self._at_eastern_border(position)
            ),
            direction.SouthWest: (
                self._at_southern_border(position) and self._at_western_border(position)
            ),
        }
        return directions.get(direction)

    def _at_northern_border(self, position: Position) -> bool:
        return position.latitude == self.min_latitude

    def _at_eastern_border(self, position: Position) -> bool:
        return position.longitude == self.max_longitude

    def _at_western_border(self, position: Position) -> bool:
        return position.longitude == self.min_longitude

    def _at_southern_border(self, position: Position) -> bool:
        return position.latitude == self.max_latitude

    def update_position(self, flying_object: FlyingObject) -> None:
        other_objects = [f for f in self.flying_objects if f != flying_object]
        for other_object in other_objects:
            if flying_object.is_colliding_with(other_object):
                self.flying_objects.remove(flying_object)
                self.flying_objects.remove(other_object)

    def get_flying_objects(self) -> List[FlyingObject]:
        return self.flying_objects.copy()
