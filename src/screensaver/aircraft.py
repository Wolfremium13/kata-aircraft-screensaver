from typing import Union

from src.screensaver.direction import Direction
from src.screensaver.flying_object import FlyingObject
from src.screensaver.position import Position
from src.screensaver.territory import Territory
from src.screensaver.validation_error import ValidationError


class Aircraft(FlyingObject):
    def __init__(
        self,
        position: Position,
        territory: Territory,
        direction: Direction = Direction.North,
    ):
        self._position = position
        self._territory = territory
        self._direction = direction

    def current_position(self) -> Position:
        return self._position.copy()

    def move(self, new_direction: Direction = None) -> None:
        self._assign_new_direction(new_direction)
        self._position = self._get_new_position_from_direction()
        self._territory.update_position(self)

    def _assign_new_direction(self, new_direction: Direction) -> None:
        if new_direction:
            self._direction = new_direction

    def _get_new_position_from_direction(self) -> Position:
        # Movement methods should be in the position class
        movements = {
            self._direction.NorthEast: self._position.go_up_right(),
            self._direction.NorthWest: self._position.go_up_left(),
            self._direction.SouthEast: self._position.go_down_right(),
            self._direction.SouthWest: self._position.go_down_left(),
            self._direction.North: self._position.go_up(),
            self._direction.South: self._position.go_down(),
            self._direction.East: self._position.go_right(),
            self._direction.West: self._position.go_left(),
        }

        direction = self._territory.change_direction_based_on_border(
            self._position, self._direction
        )
        # Check if the direction is valid after bounce?
        return movements[direction]

    def is_colliding_with(self, flying_object: FlyingObject) -> bool:
        return self._position == flying_object.current_position()

    @staticmethod
    def create(
        position: Position, territory: Territory, direction: Direction = None
    ) -> Union["Aircraft", ValidationError]:
        if (
            position.longitude > territory.max_longitude
            or position.latitude > territory.max_latitude
        ):
            return ValidationError("The position cant be out of the territory")

        if position in [p.current_position() for p in territory.get_flying_objects()]:
            return ValidationError("The position is already occupied")

        aircraft = Aircraft(position, territory, direction)
        territory.register(aircraft)
        return aircraft
