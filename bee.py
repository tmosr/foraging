#!/usr/bin/env python

from random import random as rand
import matplotlib.pyplot as plt
import numpy as np
from math import *

class Bee:
    def __init__(self,x,y,mü):
        self.x = X
        self.y = y
        self.capacity = CAPA
        self.load = 0
        self.rv = rvision
        self.mü = 1 + rand()*4
        self.ad = compute_a()
        self.cd = 0
    
    def compute_a(self):
        a_ok = FALSE
        while not a_ok:
            a = min_dist*rand()**(-1/(rand()*2))
            a_ok = a >= min_dist
        return a
    
    def do_actions(self):
        self.look_for_food()
        self.move()
        self.collect()
    
    def look_for_food(self):
        pass
        # futter in radius self.rv?
        # wert speichern
                           
    def move(self):
        # if futter in umgebung
            #fliege direkt zur futterquelle
            self.cd = 0
            self.compute_a()
            
        elif self.cd >= self.ad:
            self.cd = 0
            self.reorientate()
            
        else:
            # fliege ein schritt weiter in diese richtung
                self.cd += 1
            
    def reorientate():
        self.compute_a()
        self.move()
        
    def collect(self):
        # wenn aktuelles feld eine futterquelle
            self.load += 1
            if self.load >= self.capacity:
                self.x = x_hive
                self.y = y_hive
        
CAPA = 10
min_dist = 1
rvision = 1
x_hive = 0
y_hive = 0


