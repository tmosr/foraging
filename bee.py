#!/usr/bin/env python

from random import random as rand
import matplotlib.pyplot as plt
import numpy as np
from math import *

class Bee:
    def __init__(self, x, y, mu, grid):
        self.x = x
        self.y = x

        self.x_hive = x
        self.y_hive = y

        self.food = 0

        self.grid = grid

        self.min_dist = 1
        self.capacity = 10
        self.load = 0
        self.rv = 1
        self.mu = mu
        self.ad = self.compute_a()
        self.angle = self.compute_angle()
        self.cd = 0

    def compute_a(self):
        a_ok = False
        while not a_ok:
            a = self.min_dist*rand()**(-1/(rand()*2))
            a_ok = a >= self.min_dist
        return a

    def compute_angle(self):
        angle = rand()*2*pi
        return angle

    def do_actions(self):
        self.look_for_food()
        self.move()
        self.collect()

    def look_for_food(self):
        food = self.grid

        upleft = food[self.x-1][self.y+1]
        upmid = food[self.x][self.y+1]
        upright = food[self.x+1][self.y+1]

        midleft = food[self.x-1][self.y]
        centre = food[self.x][self.y]
        midright = food[self.x+1][self.y]

        downleft = food[self.x-1][self.y-1]
        downmid = food[self.x-1][self.y-1]
        downright = food[self.x-1][self.y-1]

        near_food = upleft+upmid+upright+midleft+centre+midright+downleft+downmid+downright

        if near_food >=1:
            r = rand()
            if r < (centre)/near_food:
                pass
            elif r < (centre+midleft)/near_food:
                self.x -= 1
            elif r < (centre+midleft+midright)/near_food:
                self.x += 1
            elif r < (centre+midleft+midright+upleft)/near_food:
                self.x -= 1
                self.y += 1
            elif r < (centre+midleft+midright+upleft+upmid)/near_food:
                self.y += 1
            elif r < (centre+midleft+midright+upleft+upmid+upright)/near_food:
                self.x += 1
                self.y += 1
            elif r < (centre+midleft+midright+upleft+upmid+upright+downleft)/near_food:
                self.x -= 1
                self.y -= 1
            elif r < (centre+midleft+midright+upleft+upmid+upright+downleft+downmid)/near_food:
                self.y -= 1
            elif r < (centre+midleft+midright+upleft+upmid+upright+downleft+downmid+downright)/near_food:
                self.x += 1
                self.y -= 1

    def move(self):
        if self.grid[self.x][self.y] >=1:
            self.cd = 0
            self.ad = self.compute_a()
            self.angle = self.compute_angle()

        elif self.cd >= self.ad:
            self.cd = 0
            self.reorientate()

        else:
            self.x += cos(self.angle)
            self.y += sin(self.angle)
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
