import pytest
from assertpy import assert_that

from src.screensaver.aircraft import Aircraft
from src.screensaver.direction import Direction
from src.screensaver.movement import Movement
from src.screensaver.position import Position
from src.screensaver.territory import Territory

TERRITORY = Territory(max_longitude=10, max_latitude=10)
AIRCRAFT_POSITION = Position(longitude=5, latitude=5)


@pytest.mark.parametrize(
    "direction,expected_position",
    [
        (Direction.North, Movement(AIRCRAFT_POSITION).go_up),
        (Direction.South, Movement(AIRCRAFT_POSITION).go_down),
        (Direction.East, Movement(AIRCRAFT_POSITION).go_right),
        (Direction.West, Movement(AIRCRAFT_POSITION).go_left),
        (Direction.NorthEast, Movement(AIRCRAFT_POSITION).go_up_right),
        (Direction.NorthWest, Movement(AIRCRAFT_POSITION).go_up_left),
        (Direction.SouthEast, Movement(AIRCRAFT_POSITION).go_down_right),
        (Direction.SouthWest, Movement(AIRCRAFT_POSITION).go_down_left),
    ],
)
def test_aircraft_moves_based_on_a_certain_direction_should(
    direction: Direction, expected_position: Position
):
    an_aircraft = Aircraft.create(AIRCRAFT_POSITION, TERRITORY)

    an_aircraft.move(direction)

    assert_that(an_aircraft.current_position()).is_equal_to(expected_position)
