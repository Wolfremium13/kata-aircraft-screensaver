import unittest

from assertpy import assert_that

from src.screensaver.aircraft import Aircraft
from src.screensaver.direction import Direction
from src.screensaver.position import Position
from src.screensaver.territory import Territory
from src.screensaver.validation_error import ValidationError


class TestAircraft(unittest.TestCase):
    def test_aircraft_cant_be_positioned_out_of_the_territory(self):
        an_aircraft = Aircraft.create(
            Position(longitude=5000, latitude=5000),
            Territory(max_longitude=200, max_latitude=200),
        )

        assert_that(an_aircraft).is_instance_of(ValidationError)

    def test_aircraft_changes_position_when_moving(self):
        an_aircraft = Aircraft.create(
            Position(longitude=5, latitude=5),
            Territory(max_longitude=200, max_latitude=200),
        )

        an_aircraft.move(Direction.NorthEast)

        assert_that(an_aircraft.current_position()).is_equal_to(
            Position(longitude=6, latitude=4)
        )

    def test_aircraft_keeps_the_direction(self):
        an_aircraft = Aircraft.create(
            Position(longitude=5, latitude=5),
            Territory(max_longitude=200, max_latitude=200),
            Direction.North,
        )

        an_aircraft.move()
        an_aircraft.move()

        assert_that(an_aircraft.current_position()).is_equal_to(
            Position(longitude=5, latitude=3)
        )

    def test_there_could_be_many_aircrafts_in_the_territory(self):
        territory = Territory(max_longitude=6, max_latitude=6)
        Aircraft.create(Position(longitude=3, latitude=1), territory)
        Aircraft.create(Position(longitude=4, latitude=1), territory)

        assert_that(len(territory.get_flying_objects())).is_equal_to(2)

    def test_aircraft_explote_and_disappear_when_they_collide_with_another_aircraft(
        self,
    ):
        territory = Territory(max_longitude=6, max_latitude=6)
        Aircraft.create(Position(longitude=3, latitude=1), territory)
        another_aircraft = Aircraft.create(Position(longitude=4, latitude=1), territory)

        another_aircraft.move(Direction.West)

        assert_that(territory.get_flying_objects()).is_empty()


class AircraftMovementWithDirectionShould(unittest.TestCase):
    def test_aircraft_moves_north(self):
        territory = Territory()
        an_aircraft = Aircraft.create(Position(longitude=0, latitude=1), territory)

        an_aircraft.move(Direction.North)

        assert_that(an_aircraft.current_position()).is_equal_to(
            Position(longitude=0, latitude=2)
        )

    def test_aircraft_moves_south(self):
        territory = Territory()
        an_aircraft = Aircraft.create(Position(longitude=0, latitude=1), territory)

        an_aircraft.move(Direction.South)

        assert_that(an_aircraft.current_position()).is_equal_to(
            Position(longitude=0, latitude=0)
        )

    def test_aircraft_moves_east(self):
        territory = Territory()
        an_aircraft = Aircraft.create(Position(longitude=1, latitude=0), territory)

        an_aircraft.move(Direction.East)

        assert_that(an_aircraft.current_position()).is_equal_to(
            Position(longitude=0, latitude=0)
        )

    def test_aircraft_moves_west(self):
        territory = Territory()
        an_aircraft = Aircraft.create(Position(longitude=1, latitude=0), territory)

        an_aircraft.move(Direction.West)

        assert_that(an_aircraft.current_position()).is_equal_to(
            Position(longitude=2, latitude=0)
        )

    def test_aircraft_moves_north_west(self):
        territory = Territory()
        an_aircraft = Aircraft.create(Position(longitude=1, latitude=1), territory)

        an_aircraft.move(Direction.NorthWest)

        assert_that(an_aircraft.current_position()).is_equal_to(
            Position(longitude=0, latitude=2)
        )

    def test_aircraft_moves_north_east(self):
        territory = Territory()
        an_aircraft = Aircraft.create(Position(longitude=0, latitude=0), territory)

        an_aircraft.move(Direction.NorthEast)

        assert_that(an_aircraft.current_position()).is_equal_to(
            Position(longitude=1, latitude=1)
        )

    def test_aircraft_moves_south_east(self):
        territory = Territory()
        an_aircraft = Aircraft.create(Position(longitude=1, latitude=1), territory)

        an_aircraft.move(Direction.SouthEast)

        assert_that(an_aircraft.current_position()).is_equal_to(
            Position(longitude=2, latitude=0)
        )

    def test_aircraft_moves_south_west(self):
        territory = Territory()
        an_aircraft = Aircraft.create(Position(longitude=1, latitude=1), territory)

        an_aircraft.move(Direction.SouthWest)

        assert_that(an_aircraft.current_position()).is_equal_to(
            Position(longitude=0, latitude=0)
        )


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
