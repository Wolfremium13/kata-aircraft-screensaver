from unittest import TestCase

from assertpy import assert_that

from src.screensaver.aircraft import Aircraft
from src.screensaver.direction import Direction
from src.screensaver.position import Position
from src.screensaver.territory import Territory
from src.screensaver.validation_error import ValidationError


class AircraftTerritoryShould(TestCase):
    def setUp(self) -> None:
        self.territory = Territory()
        self.initial_position = Position(longitude=5, latitude=5)
        return super().setUp()

    def tearDown(self) -> None:
        self.territory.flying_objects.clear()
        return super().tearDown()

    def test_aircraft_cant_be_positioned_out_of_the_territory(self):
        far_away_position = Position(longitude=1000, latitude=1000)
        an_aircraft = Aircraft.create(
            far_away_position,
            self.territory,
        )

        assert_that(an_aircraft).is_instance_of(ValidationError)

    def test_aircraft_keeps_the_direction(self):
        an_aircraft = Aircraft.create(
            self.initial_position,
            self.territory,
            Direction.North,
        )

        an_aircraft.move()
        an_aircraft.move()

        first_move_position = self.initial_position.go_up()
        second_move_position = first_move_position.go_up()
        assert_that(an_aircraft.current_position()).is_equal_to(second_move_position)

    def test_aircraft_explote_and_disappear_when_they_collide_with_another_aircraft(
        self,
    ):
        Aircraft.create(self.initial_position, self.territory)
        another_aircraft = Aircraft.create(
            self.initial_position.go_right(), self.territory
        )

        another_aircraft.move(Direction.West)

        assert_that(self.territory.get_flying_objects()).is_empty()

    def test_aircraft_cannot_be_registered_with_another_aircraft_at_the_same_place(
        self,
    ):
        Aircraft.create(self.initial_position, self.territory)
        another_aircraft = Aircraft.create(self.initial_position, self.territory)

        assert_that(another_aircraft).is_instance_of(ValidationError)

    def test_there_could_be_many_flying_objects_in_the_territory(self):
        number_of_aircraft = 2
        Aircraft.create(self.initial_position, self.territory)
        Aircraft.create(self.initial_position.go_down_right(), self.territory)

        assert_that(len(self.territory.get_flying_objects())).is_equal_to(
            number_of_aircraft
        )
