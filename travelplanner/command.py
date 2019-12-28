#!/usr/bin/env python
from argparse import ArgumentParser
from .route import Route
from .journey import Journey
from travelplanner import read_passengers


def process():
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
        print(route.timetable(args.speed))
    else:
        print(route.timetable())

    passengers = read_passengers(args.passfile)
    passengers_number = len(passengers)
    journey = Journey(passengers, route)
    for i in range(passengers_number):
        travel_time = journey.travel_time(i)
        if travel_time['bus'] == 0:
            print(
                f"Passenger {i} need to walk to the destination. It costs {travel_time['walk']} mins.")
        else:
            print(
                f"Passenger need to walk and take the bus. It costs {travel_time['walk']} mins for walk and {travel_time['bus']} mins for bus.")

    if args.saveplots:
        route.plot_map(savefig=True)
        journey.plot_bus_load(savefig=True)


if __name__ == "__main__":
    process()
