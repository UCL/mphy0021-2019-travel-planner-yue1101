#!/usr/bin/env python
from argparse import ArgumentParser
from .route import Route
from .journey import Journey
from travelplanner import read_passengers


def process():
    '''
    The process of command 'bussimula'
    '''
    parser = ArgumentParser(
        description="Generate Info for Route and Passenger")
    parser.add_argument('routefile')
    parser.add_argument('passfile')
    parser.add_argument('--speed', help='Bus Speed (mins/grid)')
    parser.add_argument(
        '--saveplots', help='Plot and save map route and evolution of the load', action='store_true')
    args = parser.parse_args()

    route = Route(args.routefile)
    if args.speed:
        print('Stops: minutes from start')
        print(route.timetable(args.speed))
    else:
        print('Stops: minutes from start')
        print(route.timetable())

    passengers = read_passengers(args.passfile)
    passengers_number = len(passengers)
    journey = Journey(passengers, route)
    for i in range(passengers_number):
        travel_time = journey.travel_time(i)
        print(f'Trip for passenger: {i}')
        start, end = journey.passenger_trip(passengers[i])
        if travel_time['bus'] == 0:
            print(f'Walk from {start[1]} to {end[1]}, donot take a bus.')
            print(f"Total time of travel: {travel_time['walk']:3.2f} minutes")
        else:
            print(f'Walk {start[0]:3.2f} units to stop {start[1]},')
            print(f'get on the bus and alite at stop {end[1]} and ')
            print(f'walk {end[0]:3.2f} units to your destination.')
            print(
                f'Total time of travel: {sum(travel_time.values()):3.2f} minutes')

    if args.saveplots:
        route.plot_map(savefig=True)
        journey.plot_bus_load(savefig=True)


if __name__ == "__main__":
    process()
