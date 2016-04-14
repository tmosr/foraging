#!/usr/bin/env python

from random import random as rand
from random import *
import numpy as np
from math import *

class BeeSpeed:
    def __init__(self, x, y, mu, grid):
        self.x = x
        self.y = y

        self.x_hive = x
        self.y_hive = y

        self.grid = grid
        self.size = self.grid.shape[0]

        self.theta = 0
        self.min_dist = 1
        self.capacity = 10
        self.load = 0
        self.rv = 3
        self.mu = mu

        self.dists = []
        self.travel_dist = 0

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

        dx = dist*cos(theta)
        dy = dist*sin(theta)

        food_pos = self.food_in_sight(dx, dy)
        if len(food_pos) > 0:
            x = food_pos[0][0][0]
            y = food_pos[0][0][1]

            d = food_pos[0][1]

        else:
            self.x = round(self.x + dx) % self.size
            self.y = round(self.y + dy) % self.size
            # append mean dist
            d = sqrt(dx**2 + dy**2)

        self.dists.append(d)
        self.travel_dist += d

    def food_in_sight(self, theta, dist):
        v = self.rv

        x = self.x + v*cos(theta)
        y = self.y + v*sin(theta)

        pos = []

        dist = min(dist, sqrt(2)*dist)

        d = 0
        while d < int(dist) and (len(pos) == 0 or d > int(dist/2)):
            x = round(self.x + d*cos(theta)) % self.size
            y = round(self.y + d*sin(theta)) % self.size
            dsx = round(x - v*cos(theta)) % self.size
            dsy = round(y - v*sin(theta)) % self.size
            for t in range(2*v):
                dx = (round(t*cos(theta - pi/2)) + x) % self.size
                dy = (round(t*sin(theta - pi/2)) + y) % self.size

                if self.grid[dx][dy] > 1:
                    p1 = (dx, dy)
                    p2 = (x,y)
                    pos.append([p1, self.periodic_dist(p1,p2)])
            d += 1
        return sorted(pos, key=lambda d: d[1])

    def periodic_dist(self, p1, p2):
        dx = p1[0]-p2[0]
        if dx > self.size/2:
            dx = self.size - dx

        dy = p1[1]-p2[1]
        if dy > self.size/2:
            dy = self.size - dy

        return sqrt(dy**2 + dx**2)

    def collect(self):
        if self.grid[self.x][self.y] >=1:
            self.grid[self.x][self.y] -= 1
            self.load += 1
            if self.load >= self.capacity:
                self.x = self.x_hive
                self.y = self.y_hive
