from enum import Enum


class Direction(Enum):
    North = 1
    South = 2
    East = 3
    West = 4
    NorthEast = 5
    NorthWest = 6
    SouthEast = 7
    SouthWest = 8

    def opposite(self) -> "Direction":
        opposite_directions = {
            self.North: self.South,
            self.South: self.North,
            self.East: self.West,
            self.West: self.East,
            self.NorthEast: self.SouthWest,
            self.NorthWest: self.SouthEast,
            self.SouthEast: self.NorthWest,
            self.SouthWest: self.NorthEast,
        }
        return opposite_directions[self]
