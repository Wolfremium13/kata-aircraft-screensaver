from typing import Union

from src.screensaver.direction import Direction
from src.screensaver.flying_object import FlyingObject
from src.screensaver.movement import PositionMovement
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
        self._position_movement = PositionMovement(position)

    def current_position(self) -> Position:
        return self._position.copy()

    def move(self, new_direction: Direction = None) -> None:
        self._assign_new_direction(new_direction)
        new_position: Position = self._position
        match self._direction:
            case self._direction.NorthEast:
                new_position = self._position_movement.go_up_right
            case self._direction.NorthWest:
                new_position = self._position_movement.go_up_left
            case self._direction.SouthEast:
                new_position = self._position_movement.go_down_right
            case self._direction.SouthWest:
                new_position = self._position_movement.go_down_left
            case self._direction.North:
                new_position = self._position_movement.go_up
            case self._direction.South:
                new_position = self._position_movement.go_down
            case self._direction.East:
                new_position = self._position_movement.go_right
            case self._direction.West:
                new_position = self._position_movement.go_left

        self._position = new_position
        self._territory.update_position(self)

    def _assign_new_direction(self, new_direction: Direction) -> None:
        if new_direction:
            self._direction = new_direction

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

        aircraft = Aircraft(position, territory, direction)
        territory.register(aircraft)
        return aircraft
