#!/usr/bin/env python

from hive import *
from bee import *
from random import random as rand
import numpy as np

class HiveCom(Hive):
    def __init__(self, x, y, n_bees, grid_size, grid):

        self.directions = []
        Hive.__init__(self, x, y, n_bees, grid_size, grid)

    def assign_settings(self, bee):
        Hive.assign_settings(self, bee)

        # direction
        if len(self.directions) == 0:
            new_angle = bee.compute_angle()
        else:
            new_angle = self.directions.pop()

        bee.angle = new_angle

    def load_settings_from(self, bee):
            self.mus.append([self.mu_counter, bee.mu])
            self.directions.append(bee.message)
            self.assign_settings(bee)


