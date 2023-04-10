from unittest import TestCase

from assertpy import assert_that

from src.screensaver.aircraft import Aircraft
from src.screensaver.direction import Direction
from src.screensaver.position import Position
from src.screensaver.territory import Territory


class BounceDirectionShould(TestCase):
    def setUp(self) -> None:
        self.initial_position = Position(longitude=0, latitude=0)
        self.empty_territory = Territory(max_longitude=0, max_latitude=0)
        self.territory_with_longitude = Territory(max_longitude=5, max_latitude=0)
        self.territory_with_latitude = Territory(max_longitude=0, max_latitude=5)
        self.aircraft_position_with_longitude = Position(longitude=1, latitude=0)
        self.aircraft_position_with_latitude = Position(longitude=0, latitude=1)
        return super().setUp()

    def tearDown(self) -> None:
        self.empty_territory.flying_objects.clear()
        self.territory_with_longitude.flying_objects.clear()
        self.territory_with_latitude.flying_objects.clear()
        return super().tearDown()

    def test_bounce_back_direction_at_the_north_territory_border(self):
        an_aircraft = Aircraft.create(self.initial_position, self.empty_territory)

        an_aircraft.move(Direction.North)

        assert_that(an_aircraft.current_direction()).is_equal_to(Direction.South)

    def test_bounce_back_direction_at_the_south_territory_border(self):
        an_aircraft = Aircraft.create(self.initial_position, self.empty_territory)

        an_aircraft.move(Direction.South)

        assert_that(an_aircraft.current_direction()).is_equal_to(Direction.North)

    def test_bounce_back_direction_at_the_east_territory_border(self):
        an_aircraft = Aircraft.create(self.initial_position, self.empty_territory)

        an_aircraft.move(Direction.East)

        assert_that(an_aircraft.current_direction()).is_equal_to(Direction.West)

    def test_bounce_back_direction_at_the_west_territory_border(self):
        an_aircraft = Aircraft.create(self.initial_position, self.empty_territory)

        an_aircraft.move(Direction.West)

        assert_that(an_aircraft.current_direction()).is_equal_to(Direction.East)

    def test_bounce_back_direction_at_the_north_west_territory_border(self):
        an_aircraft = Aircraft.create(self.initial_position, self.empty_territory)

        an_aircraft.move(Direction.NorthWest)

        assert_that(an_aircraft.current_direction()).is_equal_to(Direction.SouthEast)

    def test_bounce_back_direction_at_the_north_east_territory_border(self):
        an_aircraft = Aircraft.create(self.initial_position, self.empty_territory)

        an_aircraft.move(Direction.NorthEast)

        assert_that(an_aircraft.current_direction()).is_equal_to(Direction.SouthWest)

    def test_bounce_back_direction_at_the_south_west_territory_border(self):
        an_aircraft = Aircraft.create(self.initial_position, self.empty_territory)

        an_aircraft.move(Direction.SouthWest)

        assert_that(an_aircraft.current_direction()).is_equal_to(Direction.NorthEast)

    def test_bounce_back_direction_at_the_south_east_territory_border(self):
        an_aircraft = Aircraft.create(self.initial_position, self.empty_territory)

        an_aircraft.move(Direction.SouthEast)

        assert_that(an_aircraft.current_direction()).is_equal_to(Direction.NorthWest)

    def test_bounce_diagonally_at_the_north_territory_border_when_direction_its_north_west_and_have_latitude_in_territory(
        self,
    ):
        an_aircraft = Aircraft.create(
            self.aircraft_position_with_latitude, self.territory_with_latitude
        )

        an_aircraft.move(Direction.NorthWest)

        assert_that(an_aircraft.current_direction()).is_equal_to(Direction.NorthEast)

    def test_bounce_diagonally_at_the_north_territory_border_when_direction_its_north_west_and_have_longitude_in_territory(
        self,
    ):
        an_aircraft = Aircraft.create(
            self.aircraft_position_with_longitude, self.territory_with_longitude
        )

        an_aircraft.move(Direction.NorthWest)

        assert_that(an_aircraft.current_direction()).is_equal_to(Direction.SouthWest)

    def test_bounce_diagonally_at_the_south_territory_border_when_direction_its_south_west_and_have_latitude_in_territory(
        self,
    ):
        an_aircraft = Aircraft.create(
            self.aircraft_position_with_latitude, self.territory_with_latitude
        )

        an_aircraft.move(Direction.SouthWest)

        assert_that(an_aircraft.current_direction()).is_equal_to(Direction.SouthEast)

    def test_bounce_diagonally_at_the_south_territory_border_when_direction_its_south_west_and_have_longitude_in_territory(
        self,
    ):
        an_aircraft = Aircraft.create(
            self.aircraft_position_with_longitude, self.territory_with_longitude
        )

        an_aircraft.move(Direction.SouthWest)

        assert_that(an_aircraft.current_direction()).is_equal_to(Direction.NorthWest)

    def test_bounce_diagonally_at_the_south_territory_border_when_direction_its_south_east_and_have_latitude_in_territory(
        self,
    ):
        an_aircraft = Aircraft.create(
            self.aircraft_position_with_latitude, self.territory_with_latitude
        )

        an_aircraft.move(Direction.SouthEast)

        assert_that(an_aircraft.current_direction()).is_equal_to(Direction.SouthWest)

    def test_bounce_diagonally_at_the_south_territory_border_when_direction_its_south_east_and_have_longitude_in_territory(
        self,
    ):
        an_aircraft = Aircraft.create(
            self.aircraft_position_with_longitude, self.territory_with_longitude
        )

        an_aircraft.move(Direction.SouthEast)

        assert_that(an_aircraft.current_direction()).is_equal_to(Direction.NorthEast)

    def test_bounce_diagonally_at_the_north_territory_border_when_direction_its_north_east_and_have_latitude_in_territory(
        self,
    ):
        an_aircraft = Aircraft.create(
            self.aircraft_position_with_latitude, self.territory_with_latitude
        )

        an_aircraft.move(Direction.NorthEast)

        assert_that(an_aircraft.current_direction()).is_equal_to(Direction.SouthWest)

    def test_bounce_diagonally_at_the_north_territory_border_when_direction_its_north_east_and_have_longitude_in_territory(
        self,
    ):
        an_aircraft = Aircraft.create(
            self.aircraft_position_with_longitude, self.territory_with_longitude
        )

        an_aircraft.move(Direction.NorthEast)

        assert_that(an_aircraft.current_direction()).is_equal_to(Direction.SouthEast)
