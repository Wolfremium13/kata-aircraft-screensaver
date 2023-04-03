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
        new_position: Position = self._position
        match self._direction:
            case self._direction.NorthEast:
                if self._territory.at_northern_border(self._position):
                    new_position = Position(
                        self._position.longitude + 1, self._position.latitude + 1
                    )
                elif self._territory.at_eastern_border(self._position):
                    new_position = Position(
                        self._position.longitude - 1, self._position.latitude - 1
                    )
                else:
                    new_position = Position(
                        self._position.longitude + 1, self._position.latitude - 1
                    )
            case self._direction.NorthWest:
                # Proposal: develop bounces with TDD for all directions
                new_position = Position(
                    self._position.longitude - 1, self._position.latitude - 1
                )
            case self._direction.SouthEast:
                new_position = Position(
                    self._position.longitude + 1, self._position.latitude + 1
                )
            case self._direction.SouthWest:
                new_position = Position(
                    self._position.longitude - 1, self._position.latitude + 1
                )
            case self._direction.North:
                new_position = Position(
                    self._position.longitude, self._position.latitude - 1
                )
            case self._direction.South:
                new_position = Position(
                    self._position.longitude, self._position.latitude + 1
                )
            case self._direction.East:
                new_position = Position(
                    self._position.longitude + 1, self._position.latitude
                )
            case self._direction.West:
                if self._territory.at_western_border(self._position):
                    new_position = Position(
                        self._position.longitude + 1, self._position.latitude
                    )
                else:
                    new_position = Position(
                        self._position.longitude - 1, self._position.latitude
                    )
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
