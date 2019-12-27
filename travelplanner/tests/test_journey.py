from travelplanner.journey import Journey
from travelplanner.route import Route
from travelplanner import read_passengers
from pytest import approx


def test_constructor():
    route = Route('travelplanner/tests/random_route.csv').read_routes()
    passengers = read_passengers('travelplanner/tests/random_passengers.csv')
    journey = Journey(route, passengers)
    assert journey.route == route
    assert journey.passenger == passengers


def test_passenger_trip():
    route = Route('travelplanner/tests/random_route.csv').read_routes()
    passengers = read_passengers('travelplanner/tests/random_passengers.csv')
    journey = Journey(route, passengers)
    passenger = passengers[0]
    assert journey.passenger_trip(passenger) == (
        (1.4142135623730951, 'C'), (15.231546211727817, 'A'))


def test_travel_time():
    passenger_id = 0
    route = Route('travelplanner/tests/random_route.csv')
    passengers = read_passengers('travelplanner/tests/random_passengers.csv')
    total_time = Journey(route, passengers).travel_time(passenger_id)
    assert total_time == approx(56.3948, abs=1e-4)
