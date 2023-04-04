import unittest

from assertpy import assert_that

from src.screensaver.aircraft import Aircraft
from src.screensaver.direction import Direction
from src.screensaver.position import Position
from src.screensaver.territory import Territory


class AircraftMovementWithDirectionShould(unittest.TestCase):
    def setUp(self) -> None:
        self.territory = Territory()
        return super().setUp()

    def test_aircraft_moves_north(self):
        an_aircraft = Aircraft.create(Position(longitude=0, latitude=1), self.territory)

        an_aircraft.move(Direction.North)

        assert_that(an_aircraft.current_position()).is_equal_to(
            Position(longitude=0, latitude=2)
        )

    def test_aircraft_moves_south(self):
        an_aircraft = Aircraft.create(Position(longitude=0, latitude=1), self.territory)

        an_aircraft.move(Direction.South)

        assert_that(an_aircraft.current_position()).is_equal_to(
            Position(longitude=0, latitude=0)
        )

    def test_aircraft_moves_east(self):
        an_aircraft = Aircraft.create(Position(longitude=1, latitude=0), self.territory)

        an_aircraft.move(Direction.East)

        assert_that(an_aircraft.current_position()).is_equal_to(
            Position(longitude=2, latitude=0)
        )

    def test_aircraft_moves_west(self):
        an_aircraft = Aircraft.create(Position(longitude=1, latitude=0), self.territory)

        an_aircraft.move(Direction.West)

        assert_that(an_aircraft.current_position()).is_equal_to(
            Position(longitude=0, latitude=0)
        )

    def test_aircraft_moves_north_west(self):
        an_aircraft = Aircraft.create(Position(longitude=1, latitude=1), self.territory)

        an_aircraft.move(Direction.NorthWest)

        assert_that(an_aircraft.current_position()).is_equal_to(
            Position(longitude=0, latitude=2)
        )

    def test_aircraft_moves_north_east(self):
        an_aircraft = Aircraft.create(Position(longitude=0, latitude=0), self.territory)

        an_aircraft.move(Direction.NorthEast)

        assert_that(an_aircraft.current_position()).is_equal_to(
            Position(longitude=1, latitude=1)
        )

    def test_aircraft_moves_south_east(self):
        an_aircraft = Aircraft.create(Position(longitude=1, latitude=1), self.territory)

        an_aircraft.move(Direction.SouthEast)

        assert_that(an_aircraft.current_position()).is_equal_to(
            Position(longitude=2, latitude=0)
        )

    def test_aircraft_moves_south_west(self):
        an_aircraft = Aircraft.create(Position(longitude=1, latitude=1), self.territory)

        an_aircraft.move(Direction.SouthWest)

        assert_that(an_aircraft.current_position()).is_equal_to(
            Position(longitude=0, latitude=0)
        )
