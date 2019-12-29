from travelplanner.route import Route
from pytest import raises
import os


def test_constructor():
    filename = 'travelplanner/tests/random_route.csv'
    route = Route('travelplanner/tests/random_route.csv')
    assert route.filename == filename


def test_fail_read_routes():
    with raises(ValueError) as rs:
        Route('travelplanner/tests/random_route_fail.csv')
    assert rs.type == ValueError


def test_read_routes():
    route = Route('travelplanner/tests/random_route.csv')
    assert route.read_routes() == [(18, 6, 'A'),
                                   (18, 7, ''),
                                   (18, 8, ''),
                                   (18, 9, ''),
                                   (18, 10, ''),
                                   (18, 11, ''),
                                   (18, 12, ''),
                                   (18, 13, ''),
                                   (18, 14, ''),
                                   (18, 15, ''),
                                   (17, 15, ''),
                                   (16, 15, ''),
                                   (15, 15, ''),
                                   (14, 15, ''),
                                   (13, 15, ''),
                                   (12, 15, ''),
                                   (11, 15, ''),
                                   (10, 15, ''),
                                   (9, 15, ''),
                                   (8, 15, ''),
                                   (8, 14, ''),
                                   (8, 13, ''),
                                   (8, 12, 'B'),
                                   (8, 11, 'C'),
                                   (8, 10, ''),
                                   (9, 10, ''),
                                   (10, 10, ''),
                                   (10, 11, ''),
                                   (10, 12, ''),
                                   (10, 13, ''),
                                   (10, 14, ''),
                                   (10, 15, ''),
                                   (9, 15, ''),
                                   (8, 15, ''),
                                   (7, 15, 'D'),
                                   (6, 15, ''),
                                   (5, 15, ''),
                                   (4, 15, ''),
                                   (3, 15, ''),
                                   (2, 15, ''),
                                   (1, 15, ''),
                                   (0, 15, ''),
                                   (0, 16, ''),
                                   (0, 17, ''),
                                   (0, 18, ''),
                                   (0, 19, ''),
                                   (0, 20, ''),
                                   (0, 21, ''),
                                   (0, 22, ''),
                                   (0, 23, ''),
                                   (0, 24, ''),
                                   (0, 25, ''),
                                   (0, 26, ''),
                                   (0, 27, ''),
                                   (1, 27, ''),
                                   (2, 27, ''),
                                   (3, 27, ''),
                                   (4, 27, ''),
                                   (5, 27, ''),
                                   (6, 27, ''),
                                   (7, 27, ''),
                                   (8, 27, ''),
                                   (9, 27, ''),
                                   (9, 28, ''),
                                   (9, 29, ''),
                                   (9, 30, 'E'),
                                   (9, 31, ''),
                                   (9, 32, ''),
                                   (9, 33, 'F')]


def test_timetable():
    route = Route('travelplanner/tests/random_route.csv')
    assert route.timetable() == {'A': 0,
                                 'B': 220.0,
                                 'C': 230.0,
                                 'D': 340.0,
                                 'E': 650.0,
                                 'F': 680.0}


def test_route_cc():
    route = Route('travelplanner/tests/random_route.csv')
    assert route.route_cc(route.read_routes()) == (
        (18, 6), '6666666664444444444222220066666444444444' +
        '4666666666666000000000666666')


def test_plot_map():
    route = Route('travelplanner/tests/random_route.csv')
    route.plot_map(savefig=True)
    assert os.path.exists('map.png') is True
