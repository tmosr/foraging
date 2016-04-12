#!/usr/bin/env python

import numpy as np

class Food:
    def __init__(self, x, y, food_size, npp, max_food, grid):
        self.x = x
        self.y = y

        self.grid = grid
        self.npp = npp
        self.max_food = max_food

        self.food_size = food_size
        self.initiate_food()

    def initiate_food(self):
        offset = int(self.food_size / 2)
        x_size, y_size = self.grid.shape
        y_min = (self.y - offset) % y_size
        y_max = (self.y + offset) % y_size

        x_min = (self.x - offset) % x_size
        x_max = (self.x + offset) % x_size

        self.grid[x_min:x_max,y_min:y_max] += self.max_food

    def do_action(self):
        self.grow()

    def grow(self):
        offset = int(self.food_size / 2)
        x_size, y_size = self.grid.shape
        y_min = (self.y - offset) % y_size
        y_max = (self.y + offset) % y_size

        x_min = (self.x - offset) % x_size
        x_max = (self.x + offset) % x_size

        self.grid[x_min:x_max,y_min:y_max] += self.npp

        exceed = self.grid[x_min:x_max,y_min:y_max] > self.max_food
        self.grid[x_min:x_max,y_min:y_max][exceed] = self.max_food


