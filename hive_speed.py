#!/usr/bin/env python

from hive import *
from bee_speed import *

class HiveSpeed(Hive):
    def __init__(self, x, y, n_bees, grid_size, grid):
        self.bees = []
        Hive.__init__(self, x, y, n_bees, grid_size, grid)

    def init_bees(self, n_bees):
        # Mode bees
        self.bees = [BeeSpeed(self.x, self.y, (rand()*2 + 1), self.grid) \
                for _ in range(n_bees)]
