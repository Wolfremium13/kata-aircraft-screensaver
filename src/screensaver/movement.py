from dataclasses import dataclass

from src.screensaver.position import Position


@dataclass(frozen=True)
class Movement:
    _position: Position

    def go_up(self) -> Position:
        return Position(self._position.longitude, self._position.latitude - 1)

    def go_down(self) -> Position:
        return Position(self._position.longitude, self._position.latitude + 1)

    def go_right(self) -> Position:
        return Position(self._position.longitude + 1, self._position.latitude)

    def go_left(self) -> Position:
        return Position(self._position.longitude - 1, self._position.latitude)

    def go_up_right(self) -> Position:
        return Position(self._position.longitude + 1, self._position.latitude - 1)

    def go_up_left(self) -> Position:
        return Position(self._position.longitude - 1, self._position.latitude - 1)

    def go_down_right(self) -> Position:
        return Position(self._position.longitude + 1, self._position.latitude + 1)

    def go_down_left(self) -> Position:
        return Position(self._position.longitude - 1, self._position.latitude + 1)
