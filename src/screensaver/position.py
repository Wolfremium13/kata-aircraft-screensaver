from dataclasses import dataclass


@dataclass(frozen=True)
class Position:
    longitude: int = 0
    latitude: int = 0

    def copy(self):
        return Position(self.longitude, self.latitude)

    def __eq__(self, other: "Position") -> bool:
        return other.longitude == self.longitude and other.latitude == self.latitude

    def __str__(self):
        return f"Position({self.longitude},{self.latitude})"

    def go_up(self) -> "Position":
        return Position(self.longitude, self.latitude - 1)

    def go_down(self) -> "Position":
        return Position(self.longitude, self.latitude + 1)

    def go_right(self) -> "Position":
        return Position(self.longitude + 1, self.latitude)

    def go_left(self) -> "Position":
        return Position(self.longitude - 1, self.latitude)

    def go_up_right(self) -> "Position":
        return Position(self.longitude + 1, self.latitude - 1)

    def go_up_left(self) -> "Position":
        return Position(self.longitude - 1, self.latitude - 1)

    def go_down_right(self) -> "Position":
        return Position(self.longitude + 1, self.latitude + 1)

    def go_down_left(self) -> "Position":
        return Position(self.longitude - 1, self.latitude + 1)
