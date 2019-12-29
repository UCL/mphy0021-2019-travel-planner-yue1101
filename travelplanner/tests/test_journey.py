from travelplanner.journey import Journey, read_passengers
from travelplanner.route import Route
from pytest import approx


def test_constructor():
    route = Route('travelplanner/tests/random_route.csv').read_routes()
    passengers = read_passengers('travelplanner/tests/random_passengers.csv')
    journey = Journey(passengers, route)
    assert journey.route == route
    assert journey.passenger == passengers


def test_passenger_trip():
    route = Route('travelplanner/tests/random_route.csv')
    passengers = read_passengers('travelplanner/tests/random_passengers.csv')
    journey = Journey(passengers, route)
    passenger = passengers[0]
    assert journey.passenger_trip(passenger) == (
        (approx(1.4142135623730951, abs=1e-4), 'B'), (approx(10.816653826391969, abs=1e-4), 'A'))


def test_travel_time():
    passenger_id = 0
    route = Route('travelplanner/tests/random_route.csv')
    passengers = read_passengers('travelplanner/tests/random_passengers.csv')
    total_time = Journey(passengers, route).travel_time(passenger_id)
    assert total_time['bus'] == 0
    assert total_time['walk'] == approx(572.4893012, abs=1e-4)
