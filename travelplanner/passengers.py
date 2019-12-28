import math


class Passenger:
    def __init__(self, start_point, end_point, speed):
        self.start_point = start_point
        self.end_point = end_point
        self.speed = speed

    def walk_time(self):
        walk_time = math.sqrt((self.end_point[0] - self.start_point[0])**2 +
                              (self.end_point[1] - self.start_point[1])**2) * self.speed
        return walk_time
