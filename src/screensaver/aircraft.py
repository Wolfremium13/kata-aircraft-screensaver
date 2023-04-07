from typing import Union

from src.screensaver.direction import Direction
from src.screensaver.flying_object import FlyingObject
from src.screensaver.movement import Movement
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
        movement = Movement(self._position)
        is_at_territory_border = self._territory.is_at_border(
            self._position, self._direction
        )
        directions = {
            self._direction.NorthEast: (
                movement.go_down_left()
                if is_at_territory_border
                else movement.go_up_right()
            ),
            self._direction.NorthWest: (
                movement.go_down_right()
                if is_at_territory_border
                else movement.go_up_left()
            ),
            self._direction.SouthEast: (
                movement.go_up_left()
                if is_at_territory_border
                else movement.go_down_right()
            ),
            self._direction.SouthWest: (
                movement.go_up_right()
                if is_at_territory_border
                else movement.go_down_left()
            ),
            self._direction.North: (
                movement.go_down() if is_at_territory_border else movement.go_up()
            ),
            self._direction.South: (
                movement.go_up() if is_at_territory_border else movement.go_down()
            ),
            self._direction.East: (
                movement.go_left() if is_at_territory_border else movement.go_right()
            ),
            self._direction.West: (
                movement.go_right() if is_at_territory_border else movement.go_left()
            ),
        }
        return directions.get(self._direction)

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
