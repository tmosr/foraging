#!/usr/bin/env python

from hive import *

from random import random as rand

class Hive:
    def __init__(self, x, y, n_bees, grid_size, grid):
        self.x = x
        self.y = y

        self.grid_size = grid_size
        self.grid = grid

        self.bees = [Bee(x, y, (rand()*2 + 1), grid) \
                for _ in range(n_bees)]
        self.mus = []

        self.food_count = 0

    def do_action(self):
        self.calculate_mus()

        for bee in self.bees:
            bee.do_action()
            self.mus.append(bee.mu)
            self.collect(bee)


    def collect(self, bee):
        if bee.x == self.x and bee.y == self.y:
            self.food += bee.food
            bee.food = 0

            bee.mu = self.best_mu

    def calculate_mus(self):
        # bin mu collection
        self.best

