from dataclasses import dataclass

from src.screensaver.position import Position


@dataclass(frozen=True)
class Movement:
    position: Position

    @property
    def go_up(self) -> Position:
        return Position(self.position.longitude, self.position.latitude - 1)

    @property
    def go_down(self) -> Position:
        return Position(self.position.longitude, self.position.latitude + 1)

    @property
    def go_right(self) -> Position:
        return Position(self.position.longitude + 1, self.position.latitude)

    @property
    def go_left(self) -> Position:
        return Position(self.position.longitude - 1, self.position.latitude)

    @property
    def go_up_right(self) -> Position:
        return Position(self.position.longitude + 1, self.position.latitude - 1)

    @property
    def go_up_left(self) -> Position:
        return Position(self.position.longitude - 1, self.position.latitude - 1)

    @property
    def go_down_right(self) -> Position:
        return Position(self.position.longitude + 1, self.position.latitude + 1)

    @property
    def go_down_left(self) -> Position:
        return Position(self.position.longitude - 1, self.position.latitude + 1)
