from travelplanner.passengers import Passengers
from pytest import approx, raises


def test_walk_time():
    person = Passengers((2, 8), (24, 2), 13)
    time = person.walk_time()
    assert time == approx(296.4456, abs=1e-4)

def test_fail_walk_time():
    with raises(ValueError) as exc_info:
        passenger = Passengers([2, 8], (24, 2), 13)
        if type(passenger.start_point) != tuple:
            raise ValueError('Input(start_point) type is invalid!')
    assert exc_info.type == ValueError


    
