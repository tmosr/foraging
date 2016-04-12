#!/usr/bin/env python

from random import random as rand
from random import shuffle
import matplotlib.pyplot as plt
import numpy as np
from math import *

class Bee:
    def __init__(self, x, y, mu, grid):
        self.x = x
        self.y = y

        self.x_hive = x
        self.y_hive = y

        self.food = 0

        self.grid = grid
        self.size = self.grid.shape[0]

        self.min_dist = 1
        self.capacity = 10
        self.load = 0
        self.rv = 1
        self.mu = mu
        self.ad = self.compute_a()
        self.angle = self.compute_angle()
        self.cd = 0

    def compute_a(self):
        r_ok = False
        while not r_ok:
            r = rand()
            r_ok = r > 0.1
        a = self.min_dist*rand()**(-1/r*2)
        return a

    def compute_angle(self):
        angle = rand()*2*pi
        return angle

    def do_actions(self):
        self.look_around()
        self.move()
        self.collect()

    def look_around(self):
        pos = []
        for x in range(self.size):
            for y in range(self.size):
                if x**2 + y**2 < self.rv**2:
                    for p in pos:
                        if self.grid[p] >= 1:
                            pos.append((x,y))
        if len(pos) >= 1:
            shuffle(pos)
            self.x = pos[0] % self.size
            self.y = pos[1] % self.size


    def move(self):
        if self.grid[self.x][self.y] >=1:
            self.cd = 0
            self.ad = self.compute_a()
            self.angle = self.compute_angle()

        elif self.cd >= self.ad:
            self.cd = 0
            self.reorientate()

        else:
            self.x = (self.x+cos(self.angle)) % self.size
            self.y = (self.y + sin(self.angle)) % self.size
            self.cd += sqrt(cos(self.angle)**2+sin(self.angle)**2)

    def reorientate(self):
        self.compute_a()
        self.angle = self.compute_angle()
        self.move()

    def collect(self):
        if self.grid[self.x][self.y] >=1:
            self.load += 1
            if self.load >= self.capacity:
                self.x = self.x_hive
                self.y = self.y_hive
