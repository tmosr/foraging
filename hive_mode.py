#!/usr/bin/env python

from hive import *
from bee_mode import *

class HiveMode(Hive):
    def __init__(self, x, y, n_bees, grid_size, grid, vs, vf):
        Hive.__init__(self, x, y, n_bees, grid_size, grid)

        self.vs = vs
        self.vf = vf

    def init_bees(n_bees):

        # Mode bees
        self.bees = [BeeMode(x, y, self.vs, self.vf, grid) \
                for _ in range(n_bees)]

    def do_action(self):
        for bee in self.bees:
            bee.do_actions()
            self.collect(bee)
