from travelplanner.passengers import Passengers
from pytest import approx, raises


def test_constructor():
    passenger = Passengers((1, 2), (8, 12), 10)
    assert passenger.start_point == (1, 2)
    assert passenger.end_point == (8, 12)
    assert passenger.speed == 10


def test_walk_time():
    person = Passengers((2, 8), (24, 2), 13)
    time = person.walk_time()
    assert time == approx(296.4456, abs=1e-4)


def test_fail_walk_time():
    with raises(ValueError) as exc_info:
        passenger = Passengers((2, 8), (24, 2), 12)
        time = passenger.walk_time()
        if time != approx(296.4456, abs=1e-4):
            raise ValueError('Wrong inputs of passengers, please check!')
