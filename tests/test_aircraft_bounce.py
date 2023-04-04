import unittest

from assertpy import assert_that

from src.screensaver.aircraft import Aircraft
from src.screensaver.direction import Direction
from src.screensaver.position import Position
from src.screensaver.territory import Territory
from src.screensaver.validation_error import ValidationError


class AircraftBouncingShould(unittest.TestCase):
    # TODO: test if we're actually moving or bouncing on the tests
    def test_bounce_back_at_the_territory_north_border(self):
        territory = Territory(max_longitude=0, max_latitude=2)
        an_aircraft = Aircraft.create(Position(longitude=0, latitude=2), territory)

        an_aircraft.move(Direction.North)

        assert_that(an_aircraft.current_position()).is_equal_to(
            Position(longitude=0, latitude=1)
        )

    def test_bounce_back_at_the_territory_south_border(self):
        territory = Territory(max_longitude=0, max_latitude=1)
        an_aircraft = Aircraft.create(Position(longitude=0, latitude=0), territory)

        an_aircraft.move(Direction.South)

        assert_that(an_aircraft.current_position()).is_equal_to(
            Position(longitude=0, latitude=1)
        )

    def test_bounce_back_at_the_territory_east_border(self):
        territory = Territory(max_longitude=1, max_latitude=0)
        an_aircraft = Aircraft.create(Position(longitude=0, latitude=0), territory)

        an_aircraft.move(Direction.East)

        assert_that(an_aircraft.current_position()).is_equal_to(
            Position(longitude=1, latitude=0)
        )

    def test_bounce_back_at_the_territory_west_border(self):
        territory = Territory(max_longitude=1, max_latitude=0)
        an_aircraft = Aircraft.create(Position(longitude=0, latitude=0), territory)

        an_aircraft.move(Direction.West)

        assert_that(an_aircraft.current_position()).is_equal_to(
            Position(longitude=1, latitude=0)
        )

    def test_bounce_back_at_the_territory_northeast_border(self):
        territory = Territory(max_longitude=1, max_latitude=1)
        an_aircraft = Aircraft.create(Position(longitude=1, latitude=1), territory)

        an_aircraft.move(Direction.NorthEast)

        assert_that(an_aircraft.current_position()).is_equal_to(
            Position(longitude=0, latitude=0)
        )

    def test_bounce_diagonally_at_the_territory_eastern_border_when_moving_northeast(
        self,
    ):
        an_aircraft = Aircraft.create(
            Position(longitude=2, latitude=1),
            Territory(max_longitude=2, max_latitude=2),
        )

        an_aircraft.move(Direction.NorthEast)

        assert_that(an_aircraft.current_position()).is_equal_to(
            Position(longitude=1, latitude=0)
        )
