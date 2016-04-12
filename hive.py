#!/usr/bin/env python

from hive import *
from bee import *
from random import random as rand
import numpy as np

class Hive:
    def __init__(self, x, y, n_bees, grid_size, grid):
        self.x = x
        self.y = y

        self.grid_size = grid_size
        self.grid = grid

        self.bees = [Bee(x, y, (rand()*2 + 1), grid) \
                for _ in range(n_bees)]

        self.mus = []
        self.mu_scores = []
        self.mu_bins = []
        self.food_count = 0
        self.mu_counter = 0
        self.food = 0


        # how long to remember mus
        self.memory = 100

    def do_action(self):
        if len(self.mus) > 0:
            self.calculate_mus()

        for bee in self.bees:
            bee.do_actions()
            self.collect(bee)

        self.mu_counter += 1


    def collect(self, bee):
        if bee.x == self.x and bee.y == self.y:
            self.food += bee.food
            bee.food = 0
            self.mus.append([self.mu_counter, bee.mu])

            if len(self.mus) > 0:
                self.assign_mu(bee)

    def assign_mu(self, bee):
        r = rand()
        mus = self.mu_bins[p.where(self.mu_scores < r)]
        new_mu = mus[0]

        bee.mu = new_mu

    def discard_mus(self, max_age):
        i = 0
        while i < len(self.mus):
            m = self.mus[i]
            print self.mus
            if m[0] < (self.mu_counter - max_age):
                self.mus.remove(m)
            else:
                i += 1

    def calculate_mus(self):
        # discard mus older than 100
        self.discard_mus(self.memory)
        # create 100 bins
        self.mu_bins = np.linspace(min(self.mus),max(self.mus), 100)
        # create scores
        self.mu_scores = np.histogram(self.mus, bins, weights=self.mus)[0] / \
                np.histogram(data, bins)[0]
