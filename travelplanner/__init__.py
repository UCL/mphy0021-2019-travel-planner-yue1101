import numpy as np
import csv
from .passengers import Passenger


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
