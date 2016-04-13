#!/usr/bin/env python

# import project classes
from food import *
from hive import *

# import other classes
from random import random as rand
import numpy as np
import matplotlib.pyplot as plt

class World:
    def __init__(self, size):
        self.size = size
        self.grid = np.zeros([size, size])
        self.hives = []
        self.food = []

    def create_hive(self, n_hives, n_bees):
        # create hives x,y, n_bees, size, grid
        self.hives = [Hive(int(rand()*self.size), int(rand()*self.size),\
                n_bees, size, self.grid) for _ in range(n_hives)]

    def create_food(self, n_food, food_size, npp, max_food):
        # create food x,y,n,size
        self.food = [Food(int(rand()*self.size), \
            int(rand()*self.size), food_size, \
            npp, max_food, self.grid) for _ in range(n_food)]

    def step(self):
        for h in self.hives:
            h.do_action()
        for f in self.food:
            f.do_action()

size = 50
n_food = 10
food_size = 5
npp = 0.01
max_food = 1.1

tot_n_bees = 50
n_hives = 1
n_bees = int(tot_n_bees/n_hives)

w = World(size)
start = 0
stop = 100000

w.create_hive(n_hives, n_bees)
w.create_food(n_food, food_size, npp, max_food)

fg, ax = plt.subplots(1,n_hives + 1)

for i in range(start, stop):
    w.step()

    if i % 10 == 0:
        ax[0].clear()
        ax[0].set_aspect('equal')
        ax[0].axis([0, size, 0, size])
        ax[0].imshow(w.grid.T, cmap='Greens', vmin=0, vmax=max_food, \
                interpolation='nearest')

        for j in range(len(w.hives)):
            hive = w.hives[j]
            bees = hive.bees

            ax[0].plot(hive.x, hive.y, 'rd')
            ax[0].scatter([b.x for b in bees], [b.y for b in bees], \
                    cmap = 'Paired', vmin=0, vmax=n_hives, \
                    c=[j for _ in range(len(bees))])

            ax[1+j].clear()
            n, bins, patches = ax[1+j].hist([b.mu for b in hive.bees],normed=True)
            ax[1+j].axis([1, 3, min(n), max(n)])
            ax[1+j].set_aspect(2.\
                    /float(max(n)-min(n)))

        plt.draw()
        plt.pause(0.1)


