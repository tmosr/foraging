#!/usr/bin/env python

from random import random as rand
from random import *
import numpy as np
from math import *

class Bee:
    def __init__(self, x, y, mu, grid):
        self.x = x
        self.y = y

        self.x_hive = x
        self.y_hive = y

        self.grid = grid
        self.size = self.grid.shape[0]

        self.theta = rand()*2*pi

        self.min_dist = 1
        self.capacity = 10
        self.load = 0
        self.rv = 3
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

    def calc_dist(self):
        r = uniform(0.1, 2)
        return self.min_dist*rand()**(-1/r)

    def compute_angle(self):
        angle = rand()*2*pi
        return angle

    def do_actions(self):
        self.move()
        self.collect()

    def look_around(self):
        pos=[]
        for x in range(self.size):
            for y in range(self.size):
                if x**2 + y**2 < self.rv**2:
                    for p in pos:
                        if self.grid[p] >= 1:
                            pos.append((x,y))
        return pos

    def move(self):

        theta = self.compute_angle()
        dist = self.calc_dist()

        dx = dist*cos(self.theta)
        dy = dist*sin(self.theta)

        pos = self.look_around()

        self.x = int((self.x + dx) % self.size)
        self.y = int((self.y + dy) % self.size)

    def reorientate(self):
        self.ad = self.compute_a()
        self.angle = self.compute_angle()
        self.move()

    def collect(self):
        if self.grid[self.x][self.y] >=1:
            self.grid[self.x][self.y] -= 1
            self.load += 1
            if self.load >= self.capacity:
                self.x = self.x_hive
                self.y = self.y_hive
