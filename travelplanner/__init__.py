import numpy as np
import csv


def read_passengers(file):
    passengers = np.genfromtxt(file, delimiter=',', dtype='int')
    passengers = passengers.tolist()
    for i, passenger in enumerate(passengers):
        passengers[i] = ((passenger[0], passenger[1]),
                         (passenger[2], passenger[3]),
                         passenger[4])
    return passengers
