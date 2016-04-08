#!/usr/bin/env python

class Food:
    def __init__(self, x, y, food_size, grid):
        self.x = x
        self.y = y

        self.grid = grid

    def do_action(self):
        self.grow()

    def grow(self):
        offset = food_size / 2
