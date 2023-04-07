import pytest
from assertpy import assert_that

from src.screensaver.aircraft import Aircraft
from src.screensaver.direction import Direction
from src.screensaver.movement import Movement
from src.screensaver.position import Position
from src.screensaver.territory import Territory

TERRITORY = Territory(max_longitude=0, max_latitude=0)
AIRCRAFT_POSITION = Position(longitude=0, latitude=0)


@pytest.mark.parametrize(
    "direction,expected_position",
    [
        (Direction.North, Movement(AIRCRAFT_POSITION).go_down()),
        (Direction.South, Movement(AIRCRAFT_POSITION).go_up()),
        (Direction.East, Movement(AIRCRAFT_POSITION).go_left()),
        (Direction.West, Movement(AIRCRAFT_POSITION).go_right()),
    ],
)
def test_bounce_back_at_the_cardinal_territory_borders(
    direction: Direction, expected_position: Position
):
    an_aircraft = Aircraft.create(AIRCRAFT_POSITION, TERRITORY)

    an_aircraft.move(direction)

    assert_that(an_aircraft.current_position()).is_equal_to(expected_position)


@pytest.mark.parametrize(
    "direction,expected_position",
    [
        (Direction.NorthWest, Movement(AIRCRAFT_POSITION).go_down_right()),
        (Direction.SouthWest, Movement(AIRCRAFT_POSITION).go_up_right()),
        (Direction.NorthEast, Movement(AIRCRAFT_POSITION).go_down_left()),
        (Direction.SouthEast, Movement(AIRCRAFT_POSITION).go_up_left()),
    ],
)
def test_bounce_back_at_the_ordinal_territory_borders(
    direction: Direction, expected_position: Position
):
    an_aircraft = Aircraft.create(AIRCRAFT_POSITION, TERRITORY)

    an_aircraft.move(direction)

    assert_that(an_aircraft.current_position()).is_equal_to(expected_position)


TERRITORY_WITH_LONGITUDE = Territory(max_longitude=10, max_latitude=0)
TERRITORY_WITH_LATITUDE = Territory(max_longitude=0, max_latitude=10)


@pytest.mark.parametrize(
    "direction,expected_position,territory",
    [
        (
            Direction.NorthWest,
            Movement(AIRCRAFT_POSITION).go_up(),
            TERRITORY_WITH_LATITUDE,
        ),
        (
            Direction.NorthWest,
            Movement(AIRCRAFT_POSITION).go_left(),
            TERRITORY_WITH_LONGITUDE,
        ),
        (
            Direction.SouthWest,
            Movement(AIRCRAFT_POSITION).go_down(),
            TERRITORY_WITH_LATITUDE,
        ),
        (
            Direction.SouthWest,
            Movement(AIRCRAFT_POSITION).go_left(),
            TERRITORY_WITH_LONGITUDE,
        ),
        (
            Direction.SouthEast,
            Movement(AIRCRAFT_POSITION).go_down(),
            TERRITORY_WITH_LATITUDE,
        ),
        (
            Direction.SouthEast,
            Movement(AIRCRAFT_POSITION).go_right(),
            TERRITORY_WITH_LONGITUDE,
        ),
        (
            Direction.NorthEast,
            Movement(AIRCRAFT_POSITION).go_up(),
            TERRITORY_WITH_LATITUDE,
        ),
        (
            Direction.NorthEast,
            Movement(AIRCRAFT_POSITION).go_right(),
            TERRITORY_WITH_LONGITUDE,
        ),
    ],
)
def test_bounce_diagonally_at_the_cardinal_territory_borders(
    direction: Direction, expected_position: Position, territory: Territory
):
    an_aircraft = Aircraft.create(AIRCRAFT_POSITION, territory)

    an_aircraft.move(direction)

    assert_that(an_aircraft.current_position()).is_equal_to(expected_position)