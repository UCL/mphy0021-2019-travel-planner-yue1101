from travelplanner import read_passengers, read_routes


def test_read_passengers():
    passenger = read_passengers('./random_passengers.csv')
    assert passenger == [((2, 8), (24, 2), 13),
                         ((9, 0), (23, 8), 8),
                         ((1, 13), (14, 0), 14),
                         ((7, 7), (2, 5), 11),
                         ((21, 9), (0, 2), 20)]

def test_read_routes():
    route = read_routes('./random_route.csv')
    assert route == [(10, 8, 'A'), (10, 7, ''),
                     (10, 6, ''), (10, 5, ''), 
                     (10, 4, ''), (10, 3, ''), 
                     (9, 3, ''), (8, 3, ''),
                      (7, 3, ''), (6, 3, ''), 
                      (5, 3, ''), (4, 3, ''), 
                      (3, 3, ''), (3, 4, ''), 
                      (3, 5, ''), (3, 6, 'B'), 
                      (3, 7, 'C'), (4, 7, ''), 
                      (4, 8, ''), (4, 9, ''), 
                      (4, 10, ''), (4, 11, ''), 
                      (4, 12, ''), (4, 13, ''), 
                      (4, 14, ''), (3, 14, ''), 
                      (2, 14, 'D'), (1, 14, ''), 
                      (0, 14, 'E')]
    