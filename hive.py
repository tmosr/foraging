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

        self.mus = []
        self.mu_scores = []
        self.mu_bins = []
        self.food_count = 0
        self.mu_counter = 0
        self.food = 0

        # how long to remember mus
        self.memory = 10000

        self.travel_dists = []

        self.init_bees(n_bees)

    def init_bees(self, n_bees):
        # Normal bees
        self.bees = [Bee(self.x, self.y, (rand()*2 + 1), self.grid) \
                for _ in range(n_bees)]


    def do_action(self):
        try:

            if len(self.mus) > 0:
                self.calculate_mus()

            for bee in self.bees:
                bee.do_actions()
                self.collect(bee)

            self.mu_counter += 1

        except OverflowError:
            print("OverflowError")

    def collect(self, bee):
        if bee.x == self.x and bee.y == self.y:
            self.food += bee.load
            bee.load = 0
            self.load_settings_from(bee)


    def load_settings_from(self, bee):
            self.mus.append([self.mu_counter, bee.mu])
            self.travel_dists.append([bee.travel_dist, bee.mu])
            bee.travel_dist = 0
            bee.dists = []

            self.assign_settings(bee)

    def assign_settings(self, bee):
        # mu settings
        if len(self.mu_bins) != 0:
            r = rand()
            cum_scores = np.cumsum(self.mu_scores)
            mus = self.mu_bins[np.where(cum_scores < r)]
            if len(mus) == 0:
                new_mu = rand()*2 + 1
            else:
                new_mu = max(mus[-1] + (rand()-0.5)/5, 1)
                new_mu = min(new_mu, 3)
            bee.mu = new_mu

    def discard_mus(self, max_age):
        i = 0
        while i < len(self.mus):
            m = self.mus[i]
            if m[0] < (self.mu_counter - max_age):
                self.mus.remove(m)
            else:
                i += 1

    def calculate_mus(self):
        # discard mus older than memory
        self.discard_mus(self.memory)
        mus = np.array([m[1] for m in self.mus])
        # create bins
        self.mu_bins = np.linspace(np.amin(mus),np.amax(mus), int(len(mus)/10))
        # create scores
        if len(self.mu_bins) > 0:
            d = np.digitize(mus, self.mu_bins, right=True)
            b = np.bincount(d)
            self.mu_scores = np.divide(b, float(np.sum(b)))
