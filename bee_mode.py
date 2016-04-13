#!/usr/bin/env python

from random import random as rand
from random import *
import numpy as np
from math import *

class BeeMode:
    def __init__(self, x, y, vs, vf, grid):
        self.x = x
        self.y = y

        self.x_hive = x
        self.y_hive = y

        self.grid = grid
        self.size = self.grid.shape[0]

        self.vs = vs
        self.vf = vf

        self.theta = 0

        self.capacity = 10
        self.load = 0
        self.rv = 3

        self.mode = 0 # searching


    def calc_dist(self):
        if self.mode == 0:
            return self.vs
        elif self.mode == 1:
            return self.vf

    def compute_angle(self):
        angle = rand()*2*pi
        return angle

    def do_actions(self):
        self.move()
        self.collect()

    def move(self):

        theta = self.compute_angle()
        dist = self.calc_dist()

        dx = dist*cos(theta)
        dy = dist*sin(theta)

        self.x = round(self.x + dx) % self.size
        self.y = round(self.y + dy) % self.size

    def collect(self):
        if self.grid[self.x][self.y] >=1:
            self.mode = 1
            self.grid[self.x][self.y] -= 1
            self.load += 1
            if self.load >= self.capacity:
                self.mode = 0
                self.x = self.x_hive
                self.y = self.y_hive
        else:
            self.mode = 0
