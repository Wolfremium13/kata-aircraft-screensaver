from unittest import TestCase

from assertpy import assert_that

from src.screensaver.aircraft import Aircraft
from src.screensaver.direction import Direction
from src.screensaver.movement import Movement
from src.screensaver.position import Position
from src.screensaver.territory import Territory
from src.screensaver.validation_error import ValidationError
from parameterized import parameterized


class AircraftTerritoryShould(TestCase):
    AIRCRAFT_POSITION = Position(longitude=5, latitude=5)

    def setUp(self) -> None:
        self.territory = Territory()
        return super().setUp()

    def test_aircraft_cant_be_positioned_out_of_the_territory(self):
        far_away_position = Position(longitude=1000, latitude=1000)
        an_aircraft = Aircraft.create(
            far_away_position,
            self.territory,
        )

        assert_that(an_aircraft).is_instance_of(ValidationError)

    def test_aircraft_keeps_the_direction(self):
        an_aircraft = Aircraft.create(
            self.AIRCRAFT_POSITION,
            self.territory,
            Direction.North,
        )

        an_aircraft.move()
        an_aircraft.move()

        first_move_position = Movement(self.AIRCRAFT_POSITION).go_up()
        second_move_position = Movement(first_move_position).go_up()
        assert_that(an_aircraft.current_position()).is_equal_to(second_move_position)

    def test_aircraft_explote_and_disappear_when_they_collide_with_another_aircraft(
        self,
    ):
        Aircraft.create(Position(longitude=3, latitude=1), self.territory)
        another_aircraft = Aircraft.create(
            Position(longitude=4, latitude=1), self.territory
        )

        another_aircraft.move(Direction.West)

        assert_that(self.territory.get_flying_objects()).is_empty()

    def test_aircraft_explote_and_disappear_when_they_are_registered_with_another_aircraft_at_the_same_place(
        self,
    ):
        Aircraft.create(Position(longitude=3, latitude=1), self.territory)
        another_aircraft = Aircraft.create(
            Position(longitude=4, latitude=1), self.territory
        )

        another_aircraft.move(Direction.West)

        assert_that(self.territory.get_flying_objects()).is_empty()

    def test_there_could_be_many_flying_objects_in_the_territory(self):
        territory = Territory(max_longitude=6, max_latitude=6)
        Aircraft.create(Position(longitude=3, latitude=1), territory)
        Aircraft.create(Position(longitude=4, latitude=1), territory)

        assert_that(len(territory.get_flying_objects())).is_equal_to(2)


class MovementShould(TestCase):
    AIRCRAFT_POSITION = Position(longitude=5, latitude=5)

    @parameterized.expand(
        [
            (
                f"{Direction.North}",
                Direction.North,
                Movement(AIRCRAFT_POSITION).go_up(),
            ),
            (
                f"{Direction.South}",
                Direction.South,
                Movement(AIRCRAFT_POSITION).go_down(),
            ),
            (
                f"{Direction.East}",
                Direction.East,
                Movement(AIRCRAFT_POSITION).go_right(),
            ),
            (
                f"{Direction.West}",
                Direction.West,
                Movement(AIRCRAFT_POSITION).go_left(),
            ),
            (
                f"{Direction.NorthEast}",
                Direction.NorthEast,
                Movement(AIRCRAFT_POSITION).go_up_right(),
            ),
            (
                f"{Direction.NorthWest}",
                Direction.NorthWest,
                Movement(AIRCRAFT_POSITION).go_up_left(),
            ),
            (
                f"{Direction.SouthEast}",
                Direction.SouthEast,
                Movement(AIRCRAFT_POSITION).go_down_right(),
            ),
            (
                f"{Direction.SouthWest}",
                Direction.SouthWest,
                Movement(AIRCRAFT_POSITION).go_down_left(),
            ),
        ],
    )
    def test_move_aircraft_based_on_a_certain_direction(
        self, _, direction: Direction, expected_position: Position
    ):
        an_aircraft = Aircraft.create(
            self.AIRCRAFT_POSITION, Territory(max_longitude=10, max_latitude=10)
        )

        an_aircraft.move(direction)

        assert_that(an_aircraft.current_position()).is_equal_to(expected_position)


class BounceShould(TestCase):

    TERRITORY_WITH_LONGITUDE = Territory(max_longitude=5, max_latitude=0)
    TERRITORY_WITH_LATITUDE = Territory(max_longitude=0, max_latitude=5)
    AIRCRAFT_POSITION_WITH_LONGITUDE = Position(longitude=1, latitude=0)
    AIRCRAFT_POSITION_WITH_LATITUDE = Position(longitude=0, latitude=1)
    AIRCRAFT_DEFAULT_POSITION = Position(longitude=0, latitude=0)
    TERRITORY_EMPTY = Territory(max_longitude=0, max_latitude=0)

    @parameterized.expand(
        [
            (
                f"{Direction.North}",
                Direction.North,
                Movement(AIRCRAFT_DEFAULT_POSITION).go_down(),
            ),
            (
                f"{Direction.South}",
                Direction.South,
                Movement(AIRCRAFT_DEFAULT_POSITION).go_up(),
            ),
            (
                f"{Direction.East}",
                Direction.East,
                Movement(AIRCRAFT_DEFAULT_POSITION).go_left(),
            ),
            (
                f"{Direction.West}",
                Direction.West,
                Movement(AIRCRAFT_DEFAULT_POSITION).go_right(),
            ),
        ],
    )
    def test_bounce_back_at_the_cardinal_territory_borders(
        self, _, direction: Direction, expected_position: Position
    ):
        an_aircraft = Aircraft.create(
            self.AIRCRAFT_DEFAULT_POSITION, self.TERRITORY_EMPTY
        )

        an_aircraft.move(direction)

        assert_that(an_aircraft.current_position()).is_equal_to(expected_position)

    @parameterized.expand(
        [
            (
                f"{Direction.NorthWest}",
                Direction.NorthWest,
                Movement(AIRCRAFT_DEFAULT_POSITION).go_down_right(),
            ),
            (
                f"{Direction.SouthWest}",
                Direction.SouthWest,
                Movement(AIRCRAFT_DEFAULT_POSITION).go_up_right(),
            ),
            (
                f"{Direction.NorthEast}",
                Direction.NorthEast,
                Movement(AIRCRAFT_DEFAULT_POSITION).go_down_left(),
            ),
            (
                f"{Direction.SouthEast}",
                Direction.SouthEast,
                Movement(AIRCRAFT_DEFAULT_POSITION).go_up_left(),
            ),
        ],
    )
    def test_bounce_back_at_the_ordinal_territory_borders(
        self, _, direction: Direction, expected_position: Position
    ):
        an_aircraft = Aircraft.create(
            self.AIRCRAFT_DEFAULT_POSITION, self.TERRITORY_EMPTY
        )

        an_aircraft.move(direction)

        assert_that(an_aircraft.current_position()).is_equal_to(expected_position)

    @parameterized.expand(
        [
            (
                f"{Direction.NorthWest}",
                AIRCRAFT_POSITION_WITH_LATITUDE,
                Direction.NorthWest,
                Movement(AIRCRAFT_POSITION_WITH_LATITUDE).go_up(),
                TERRITORY_WITH_LATITUDE,
            ),
            (
                f"{Direction.NorthWest}",
                AIRCRAFT_POSITION_WITH_LONGITUDE,
                Direction.NorthWest,
                Movement(AIRCRAFT_POSITION_WITH_LONGITUDE).go_left(),
                TERRITORY_WITH_LONGITUDE,
            ),
            (
                f"{Direction.SouthWest}",
                AIRCRAFT_POSITION_WITH_LATITUDE,
                Direction.SouthWest,
                Movement(AIRCRAFT_POSITION_WITH_LATITUDE).go_down(),
                TERRITORY_WITH_LATITUDE,
            ),
            (
                f"{Direction.SouthWest}",
                AIRCRAFT_POSITION_WITH_LONGITUDE,
                Direction.SouthWest,
                Movement(AIRCRAFT_POSITION_WITH_LONGITUDE).go_left(),
                TERRITORY_WITH_LONGITUDE,
            ),
            (
                f"{Direction.SouthEast}",
                AIRCRAFT_DEFAULT_POSITION,
                Direction.SouthEast,
                Movement(AIRCRAFT_DEFAULT_POSITION).go_down(),
                TERRITORY_WITH_LATITUDE,
            ),
            (
                f"{Direction.SouthEast}",
                AIRCRAFT_DEFAULT_POSITION,
                Direction.SouthEast,
                Movement(AIRCRAFT_DEFAULT_POSITION).go_right(),
                TERRITORY_WITH_LONGITUDE,
            ),
            (
                f"{Direction.NorthEast}",
                AIRCRAFT_POSITION_WITH_LATITUDE,
                Direction.NorthEast,
                Movement(AIRCRAFT_POSITION_WITH_LATITUDE).go_up(),
                TERRITORY_WITH_LATITUDE,
            ),
            (
                f"{Direction.NorthEast}",
                AIRCRAFT_DEFAULT_POSITION,
                Direction.NorthEast,
                Movement(AIRCRAFT_DEFAULT_POSITION).go_right(),
                TERRITORY_WITH_LONGITUDE,
            ),
        ],
    )
    def test_bounce_diagonally_at_the_cardinal_territory_borders_when_direction_its_ordinarily(
        self,
        _,
        aircraft_position: Position,
        direction: Direction,
        expected_position: Position,
        territory: Territory,
    ):
        an_aircraft = Aircraft.create(aircraft_position, territory)

        an_aircraft.move(direction)

        assert_that(an_aircraft.current_position()).is_equal_to(expected_position)
