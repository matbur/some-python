#!/usr/bin/env python3

import random
from time import time

import matplotlib.pyplot as plt
import numpy as np

from grid import Grid

sizes = (10, 20, 40, 80)
linspace = np.linspace(.2, .8, 30)


def get_number_of_grids():
    return random.randint(50, 200)


def count_probability(size):
    all_grids = []
    for density in linspace:
        t = time()
        all_grids.append(
            [Grid(size, density) for _ in range(get_number_of_grids())]
        )
        print(time() - t, size, density, len(all_grids[-1]))

    probability = []
    for grids_n in all_grids:
        density = grids_n[0].density
        probability.append(
            (density, sum(grid.has_percolation for grid in grids_n) / len(grids_n))
        )
    return probability


def show_probability(n, probability):
    z = list(zip(*probability))
    plt.plot(*z, 'o', *z, 'k')
    plt.title('Probability for n = {}'.format(n))
    plt.xlabel('density')
    plt.ylabel('probability')
    plt.show()


def main():
    size = sizes[2]
    t = time()
    pro = count_probability(size)
    print('done in ', time() - t)
    show_probability(size, pro)


if __name__ == '__main__':
    main()
