#!/usr/bin/env python

from food import *
from hive import *
from food import *


class World:
    def __init__(self, size):
        self.size = size
        self.grid = np.array([size, size])
        self.hives = []
        self.food = []

    def create_hive(self, n_hives, n_bees):
        # create hives x,y, n_bees, size, grid
        self.hives = [Hive(int(rand()*self.size), int(rand()*self.size),\
                n_bees, size, self.grid) for _ in range(n_hive)]

    def create_food(self, n_food, food_size):
        # create food x,y,n,size
        self.food = [Food(int(rand()*self.size), \
            int(rand()*self.size)) for _ in range(n)]


size = 1000
n_food = 20
food_size = 10

tot_n_bees = 200
n_hives = 10
n_bees = tot_n_bees/n_hives

w = World(size)
start = 0
stop = 100000

w.create_hive(n_hives, n_bees)
w.create_food(n_food, food_size)

for i in range(start, stop):
    w.step()
