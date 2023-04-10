from unittest import TestCase

from assertpy import assert_that

from src.screensaver.aircraft import Aircraft
from src.screensaver.direction import Direction
from src.screensaver.movement import Movement
from src.screensaver.position import Position
from src.screensaver.territory import Territory


class MovementShould(TestCase):
    def setUp(self) -> None:
        self.initial_position = Position(longitude=5, latitude=5)
        self.territory = Territory()
        return super().setUp()

    def tearDown(self) -> None:
        self.territory.flying_objects.clear()
        return super().tearDown()

    def test_move_aircraft_to_the_north(self):
        an_aircraft = Aircraft.create(self.initial_position, self.territory)

        an_aircraft.move(Direction.North)

        assert_that(an_aircraft.current_position()).is_equal_to(
            Movement(self.initial_position).go_up()
        )

    def test_move_aircraft_to_the_south(self):
        an_aircraft = Aircraft.create(self.initial_position, self.territory)

        an_aircraft.move(Direction.South)

        assert_that(an_aircraft.current_position()).is_equal_to(
            Movement(self.initial_position).go_down()
        )

    def test_move_aircraft_to_the_east(self):
        an_aircraft = Aircraft.create(self.initial_position, self.territory)

        an_aircraft.move(Direction.East)

        assert_that(an_aircraft.current_position()).is_equal_to(
            Movement(self.initial_position).go_right()
        )

    def test_move_aircraft_to_the_west(self):
        an_aircraft = Aircraft.create(self.initial_position, self.territory)

        an_aircraft.move(Direction.West)

        assert_that(an_aircraft.current_position()).is_equal_to(
            Movement(self.initial_position).go_left()
        )

    def test_move_aircraft_to_the_north_east(self):
        an_aircraft = Aircraft.create(self.initial_position, self.territory)

        an_aircraft.move(Direction.NorthEast)

        assert_that(an_aircraft.current_position()).is_equal_to(
            Movement(self.initial_position).go_up_right()
        )

    def test_move_aircraft_to_the_north_west(self):
        an_aircraft = Aircraft.create(self.initial_position, self.territory)

        an_aircraft.move(Direction.NorthWest)

        assert_that(an_aircraft.current_position()).is_equal_to(
            Movement(self.initial_position).go_up_left()
        )

    def test_move_aircraft_to_the_south_east(self):
        an_aircraft = Aircraft.create(self.initial_position, self.territory)

        an_aircraft.move(Direction.SouthEast)

        assert_that(an_aircraft.current_position()).is_equal_to(
            Movement(self.initial_position).go_down_right()
        )

    def test_move_aircraft_to_the_south_west(self):
        an_aircraft = Aircraft.create(self.initial_position, self.territory)

        an_aircraft.move(Direction.SouthWest)

        assert_that(an_aircraft.current_position()).is_equal_to(
            Movement(self.initial_position).go_down_left()
        )
