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
                n_bees, size, self.grid) for _ in range(n_hive)]

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

size = 100
n_food = 20
n_hive = 1
food_size = 10
npp = 1
max_food = 1.1

tot_n_bees = 200
n_hives = 2
n_bees = tot_n_bees/n_hives

w = World(size)
start = 0
stop = 100000

w.create_hive(n_hives, n_bees)
w.create_food(n_food, food_size, npp, max_food)

fg, field = plt.subplots(1,1)

for i in range(start, stop):
    w.step()

    field.clear()
    field.set_aspect('equal')
    field.axis([0, size, 0, size])
    field.imshow(w.grid.T)
    for i in range(len(w.hives)):
        hive = w.hives[i]
        bees = hive.bees

        field.plot(hive.x, hive.y, 'k.')
        field.scatter([b.x for b in bees], [b.y for b in bees], \
                cmap = 'Paired', vmin=0, vmax=n_hives, \
                c=[i for _ in range(len(bees))])

    plt.draw()
    plt.pause(0.1)
