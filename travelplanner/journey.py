from travelplanner.route import Route
from travelplanner.passengers import Passenger
import matplotlib.pyplot as plt
import math
import numpy as np
import csv


def read_passengers(file):
    '''
    Transfer raw data random_passenger.csv into another format

    Parameters
    ----------
    file: .csv file
        Contains information of passengers

    Returns
    -------
    passengers: list
    '''
    passengers = np.genfromtxt(file, delimiter=',', dtype='int')
    passengers = passengers.tolist()
    for i, passenger in enumerate(passengers):
        passengers[i] = ((passenger[0], passenger[1]),
                         (passenger[2], passenger[3]),
                         passenger[4])
    return passengers


class Journey:
    '''
    Choose the route with least time for every passenger.
    Return distances walking to the start bus stop and stop name, aliting bus
        and walking to the destination and the stop name.
    Plot load.png to show the load at every bus stop.
    Print time spent on bus and walking for the passenger.
    Print average time spent on bus and walking among all the passengers.

    Parameters
    ----------
    passengers: list
        all passengers' information

    route: object
        a instance of class Route

    Methods
    -------
    passenger_trip(self, passenger)

    plot_bus_load(self, savefig=False)

    travel_time(self, passenger_id)

    print_time_stats(self)

    Detail information please see in respective method.
    '''

    def __init__(self, passengers, route):
        self.route = route
        self.passenger = passengers

    def passenger_trip(self, passenger):
        '''
        Give the start and end stops and the distances from taking the bus.

        Parameters
        ----------
        passenger: tuple,
            The information of passsenger : (start, end, speed)

        Returns
        --------
        tuple
            ((The distance passenger walking to bus stop, stop),
             (The distance passenger walking to destination alite the bus, stop))
        '''
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

    def plot_bus_load(self, savefig=False):
        '''
        Plot the number of passengers at every stop

        Parameters
        -----------
        savefig: bool, default: False
            If set savefig to True, load.png will be saved.
        '''
        stops = {step[2]: 0
                 for step in self.route.read_routes() if step[2]}
        for passenger in self.passenger:
            trip = self.passenger_trip(passenger)
            # passenger and bus have same direction.
            if trip[0][1] < trip[1][1]:
                stops[trip[0][1]] += 1
                stops[trip[1][1]] -= 1
        for i, stop in enumerate(stops):
            if i > 0:
                stops[stop] += stops[prev]
            prev = stop
        _, ax = plt.subplots()
        ax.step(range(len(stops)), list(stops.values()), where='post')
        ax.set_xticks(range(len(stops)))
        ax.set_xticklabels(list(stops.keys()))
        if savefig is True:
            plt.savefig('load.png')
        plt.show()

    def travel_time(self, passenger_id):
        '''
        Give the time needed for walking and taking the bus

        Parameters
        -----------
        passenger_id: int
            choose a random passenger id

        Returns
        -----------
        travel_walk_time: dict
            The dict has two keys: 'bus' and 'walk', and its value is corresponding time
        '''

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
        '''
        Print average time spending on bus and average time spent on walking.
        '''
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
