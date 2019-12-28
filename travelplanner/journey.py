from travelplanner.route import Route
from travelplanner import read_passengers
from travelplanner.passengers import Passenger
import matplotlib.pyplot as plt
import math


class Journey:
    def __init__(self, passengers, route):
        self.route = route
        self.passenger = passengers

    def passenger_trip(self, passenger):
        start, end, _ = passenger
        stops = [value for value in self.route.read_routes() if value[2]]
        # calculate closer stops
        # to start
        distances = [(math.sqrt((x - start[0])**2 +
                                (y - start[1])**2), stop) for x, y, stop in stops]
        min_distance1, min_distance2 = sorted(distances)[:2]
        if min_distance1 == min_distance2:
            closer_start = min_distance2
        else:
            closer_start = min(distances)
        # to end
        distances = [(math.sqrt((x - end[0])**2 +
                                (y - end[1])**2), stop) for x, y, stop in stops]
        closer_end = min(distances)
        return (closer_start, closer_end)

    def plot_bus_load(self):
        stops = {step[2]: 0
                 for step in self.route if step[2]}
        for passenger in self.passenger:
            trip = self.passenger_trip(passenger)
            stops[trip[0][1]] += 1
            stops[trip[1][1]] -= 1
        for i, stop in enumerate(stops):
            if i > 0:
                stops[stop] += stops[prev]
            prev = stop
        _, ax = plt.subplots()
        ax.step(range(len(stops)), stops.values(), where='post')
        ax.set_xticks(range(len(stops)))
        ax.set_xticklabels(list(stops.keys()))
        plt.show()

    def travel_time(self, passenger_id):
        passengers = {}
        for i, passenger in enumerate(self.passenger):
            passengers[i] = passenger
        walk_distance_stops = self.passenger_trip(passengers[passenger_id])
        bus_times = self.route.timetable()
        bus_travel = bus_times[walk_distance_stops[1][1]] - \
            bus_times[walk_distance_stops[0][1]]
        walk_travel = walk_distance_stops[0][0] * passengers[passenger_id][2] + \
            walk_distance_stops[1][0] * passengers[passenger_id][2]
        travel_walk_time = {'bus': bus_travel, 'walk': walk_travel}
        walk_time = Passenger(*passengers[passenger_id]).walk_time()
        # bus travel < 0 means the bus has opposite direction of passenger.
        if walk_time <= bus_travel + walk_travel or bus_travel < 0:
            time = walk_time
            print(f'This passenger should just walk for {time} mins.')
            return {'bus': 0, 'walk': time}
        else:
            time = bus_travel + walk_travel
            print(
                f'This passenger take a walk for {walk_travel} mins and take a bus for {bus_travel} min.')
            return travel_walk_time

    def print_time_stats(self):
        total_walking_time = 0
        total_bus_time = 0
        passengers_number = len(self.passenger)
        for i in range(passengers_number):
            time = self.travel_time(i)
            total_bus_time += time['bus']
            total_walking_time += time['walk']
        average_walking_time = total_walking_time / passengers_number
        average_bus_time = total_bus_time / passengers_number
        print(f'Average time on bus: {average_bus_time} min')
        print(f'Average walking time: {average_walking_time} min')
