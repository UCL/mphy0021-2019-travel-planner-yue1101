from travelplanner.route import Route


def test_constructor():
    filename = 'random_route.csv'
    route = Route('random_route.csv')
    assert route.filename == filename


def test_read_routes():
    route = Route('random_route.csv')
    assert route.read_routes() == [(10, 8, 'A'),
                                   (10, 7, ''),
                                   (10, 6, ''),
                                   (10, 5, ''),
                                   (10, 4, ''),
                                   (10, 3, ''),
                                   (9, 3, ''),
                                   (8, 3, ''),
                                   (7, 3, ''),
                                   (6, 3, ''),
                                   (5, 3, ''),
                                   (4, 3, ''),
                                   (3, 3, ''),
                                   (3, 4, ''),
                                   (3, 5, ''),
                                   (3, 6, 'B'),
                                   (3, 7, 'C'),
                                   (4, 7, ''),
                                   (4, 8, ''),
                                   (4, 9, ''),
                                   (4, 10, ''),
                                   (4, 11, ''),
                                   (4, 12, ''),
                                   (4, 13, ''),
                                   (4, 14, ''),
                                   (3, 14, ''),
                                   (2, 14, 'D'),
                                   (1, 14, ''),
                                   (0, 14, 'E')]


def test_timetable():
    route = Route('random_route.csv')
    assert route.timetable() == {'A': 0,
                                 'B': 150,
                                 'C': 160,
                                 'D': 260,
                                 'E': 280}


def route_cc():
    route = Route('random_route.csv')
    assert route.route_cc() == ((10, 8),
                                '2222244444446666066666664444')
