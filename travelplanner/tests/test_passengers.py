from travelplanner.passengers import Passenger
from pytest import approx, raises
import pytest
import yaml


def test_constructor():
    passenger = Passenger((1, 2), (8, 12), 10)
    assert passenger.start_point == (1, 2)
    assert passenger.end_point == (8, 12)
    assert passenger.speed == 10


def read_fixture():
    with open('./travelplanner/tests/fixture_data.yaml') as ft:
        fixtures = yaml.safe_load(ft)
    return fixtures


@pytest.mark.parametrize("fixture", read_fixture())
def test_walk_time(fixture):
    for ft in fixture:
        answer = ft.pop('answer')
        person = Passenger(**ft)
        assert person.walk_time() == answer


def test_fail_walk_time():
    with raises(ValueError) as exc_info:
        passenger = Passenger((2, 8), (24, 2), 12)
        time = passenger.walk_time()
        if time != approx(296.4456, abs=1e-4):
            raise ValueError('Wrong inputs of passengers, please check!')
    assert exc_info.type == ValueError
