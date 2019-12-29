import matplotlib.pyplot as plt
import csv
import numpy as np


class Route:
    '''
    Read the raw route.csv file into correct format.
    Return coordination and timepoint for every grid, the timetable of the bus
        and the freeman chaincode.
    Plot the bus route and every stop.

    Parameters
    ----------
    filename: .csv file
        contains information of bus route

    Methods
    -------
    read_routes(self)

    plot_map(self, savefig=False)

    timetable(self, bus_speed=10)

    route_cc(self, route)

    Detail information please see in respective method.
    '''

    def __init__(self, filename):
        self.filename = filename

    def read_routes(self):
        '''
        Transfer raw data random_route.csv into another format

        Returns
        -------
        routes: list
            Contains information of grid
        '''
        with open(self.filename) as fn:
            lines = csv.reader(fn)
            routes = [(int(line[0]), int(line[1]), line[2])
                      for line in lines]
        results = self.route_cc(routes)
        wrong_directions = ['1', '3', '5', '7']
        for cc in results[1]:
            if cc in wrong_directions:
                raise ValueError('Wrong direction! Cannot go diaganoly!')
        return routes

    def plot_map(self, savefig=False):
        '''
        Plot the bus route and every stop

        Parameters
        -----------
        savefig: bool, default: False
            If set it to True, map.png will be saved.
        '''
        route = self.read_routes()
        max_x = max([n[0] for n in route]) + 5  # adds padding
        max_y = max([n[1] for n in route]) + 5
        grid = np.zeros((max_y, max_x))
        for x, y, stop in route:
            grid[y, x] = 1
            if stop:
                grid[y, x] += 1
        _, ax = plt.subplots(1, 1)
        ax.pcolor(grid)
        ax.invert_yaxis()
        ax.set_aspect('equal', 'datalim')
        if savefig == True:
            plt.savefig('map.png')
        plt.show()

    def timetable(self, bus_speed=10):
        '''     
        Generates a timetable for a route as minutes from its first stop. 

        Parameters
        ----------
        bus_speed: int or float, default: 10
            specify bus_speed

        Returns
        -------
        stops: dict
            keys: 'bus stop name'
            values: timepoint of every stop
        '''
        route = self.read_routes()
        time = 0
        stops = {}
        for step in route:
            if step[2]:
                stops[step[2]] = time
            time += float(bus_speed)
        return stops

    def route_cc(self, route):
        r'''
        Converts a set of route into a Freeman chain code
           3  2  1
            \ | / 
        4   - C -   0
            / | \ 
           5  6  7 

        Parameters
        ----------
        route: list
            Contains information of grid

        Returns
        -------
        start: tuple
            the start coordination of bus

        ''.join(cc): string
            the chaincode of the bus
        '''
        start = route[0][:2]
        cc = []
        freeman_cc2coord = {0: (1, 0),
                            1: (1, -1),
                            2: (0, -1),
                            3: (-1, -1),
                            4: (-1, 0),
                            5: (-1, 1),
                            6: (0, 1),
                            7: (1, 1)}
        freeman_coord2cc = {val: key for key, val in freeman_cc2coord.items()}
        for b, a in zip(route[1:], route):
            x_step = b[0] - a[0]
            y_step = b[1] - a[1]
            cc.append(str(freeman_coord2cc[(x_step, y_step)]))
        return start, ''.join(cc)
