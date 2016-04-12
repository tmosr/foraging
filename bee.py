#!/usr/bin/env python

from random import random as rand
import matplotlib.pyplot as plt
import numpy as np
from math import *

class Bee:
    def __init__(self,x,y,mu):
        self.x = X
        self.y = y
        self.capacity = CAPA
        self.load = 0
        self.rv = rvision
        self.mu = 1 + rand()*4
        self.ad = compute_a()
        self.angle = compute_angle()
        self.cd = 0
    
    def compute_a(self):
        a_ok = FALSE
        while not a_ok:
            a = min_dist*rand()**(-1/(rand()*2))
            a_ok = a >= min_dist
        return a
        
    def compute_angle(self):
        angle = rand()*2*pi
        return angle
    
    def do_actions(self):
        self.look_for_food()
        self.move()
        self.collect()
    
    def look_for_food(self):
        pass
        upleft= food[self.x-1][self.y+1]
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
        if food[self.x][self.y] >=1:
            self.cd = 0
            self.ad = self.compute_a()
            self.angle = self.compute_angle()
            
        elif self.cd >= self.ad:
            self.cd = 0
            self.reorientate()
            
        else:
            self.x += cos(self.angle)
            self.y += sin(self.angle)
            self.cd += sqrt(cos(self.anlge)**2+sin(self.angle)**2)
            
    def reorientate():
        self.compute_a()
        self.angle = self.compute_angle()
        self.move()
        
    def collect(self):
        if food[self.x][self.y] >=1:
            self.load += 1
            if self.load >= self.capacity:
                self.x = x_hive
                self.y = y_hive
        
CAPA = 10
min_dist = 1
rvision = 1
x_hive = 0
y_hive = 0


