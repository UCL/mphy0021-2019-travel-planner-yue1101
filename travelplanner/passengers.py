import math


class Passenger:
    '''
    Calculate the total walking time of a person.

    Parameters
    ----------
    start: tuple
        the start coordinate of a person

    end: tuple
        the end coordinate of a person

    speed: int
        the speed of a person

    Methods
    -------
    walk_time(self)

    Detail information please see in respective method.
    '''

    def __init__(self, start, end, speed):
        self.start_point = start
        self.end_point = end
        self.speed = speed

    def walk_time(self):
        '''
        Give the total walking time of person

        Returns
        -------
        walk_time: float
            the total walking time of a person

        Examples
        ---------
        >>> from travelplanner.passengers import Passenger
        >>> Xiaoli = Passenger((0, 0), (30, 40), 10)
        >>> Xiaoli.walk_time()
        500.0
        '''
        walk_time = math.sqrt((self.end_point[0] - self.start_point[0])**2 +
                              (self.end_point[1] - self.start_point[1])**2) * self.speed
        return walk_time
