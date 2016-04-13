#!/usr/bin/env python

from hive import *
from bee_mode import *

class HiveMode(Hive):
    def __init__(self, x, y, n_bees, grid_size, grid, vs, vf):
        self.bees = []

        self.vs = vs
        self.vf = vf
        Hive.__init__(self, x, y, n_bees, grid_size, grid)

    def init_bees(self, n_bees):
        # Mode bees
        self.bees = [BeeMode(self.x, self.y, self.vs, self.vf, self.grid) \
                for _ in range(n_bees)]

    def do_action(self):
        for bee in self.bees:
            bee.do_actions()
            self.collect(bee)

    def load_mu_from(self, bee):
        pass
