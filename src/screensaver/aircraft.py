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

    def current_direction(self) -> Direction:
        return self._direction

    def move(self, given_direction: Direction = None) -> None:
        direction = given_direction or self._direction
        (
            self._direction,
            self._position,
        ) = self._territory.get_position_and_direction_based_on_borders(
            self._position, direction
        )
        self._territory.update_position(self)

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
