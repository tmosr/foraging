#!/usr/bin/env python

# import project classes
from food import *
from hive import *
from hive_com import *

# import other classes
from random import random as rand
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as cl
import matplotlib.cm as cm
from math import log

class World:
    def __init__(self, size):
        self.size = size
        self.grid = np.zeros([size, size])
        self.hives = []
        self.food = []

    def create_hive_stupid(self, n_hives, n_bees):
        # create hives x,y, n_bees, size, grid
        for _ in range(n_hives):
            self.hives.append(Hive(int(rand()*self.size), int(rand()*self.size),\
                    n_bees, size, self.grid))

    def create_hive_intelligent(self, n_hives, n_bees):
        # create hives x,y, n_bees, size, grid
        for _ in range(n_hives):
            self.hives.append(HiveCom(int(rand()*self.size), int(rand()*self.size),\
                    n_bees, size, self.grid))

    def create_food(self, n_food, food_size, npp, max_food):
        # create food x,y,n,size
        self.food = [Food(int(rand()*self.size), \
            int(rand()*self.size), food_size, \
            npp, max_food, self.grid) for _ in range(n_food)]

    def step(self):
        for h in self.hives:
            h.do_action()
        for f in self.food:
            f.do_action()

    def av_food_dist(self):
        food_dist_x=[]
        food_dist_y=[]
        for f in self.food:
            for x in range(size):
                for y in range(size):
                    for f in food_dist:
                        if f.grid[f] >= 1:
                            food_dist_x.append(x)
                            food_dist_y.append(y)
        av_x= np.mean(food_dist_x)
        av_y= np.mean(food_dist_y)
        afd = hypot(av_x,av_y)
        return afd

size = 120
n_food = 20
food_size = 8
npp = 0.01
max_food = 1.1

vs = 10
vf = 1

tot_n_bees = 120
n_hives = 2
n_bees = int(tot_n_bees/(n_hives))

w = World(size)
start = 0
stop = 100000

w.create_hive_intelligent(int(n_hives/2), n_bees)
w.create_hive_stupid(int(n_hives/2), n_bees)
l_labels = ['intelligent', 'stupid']
w.create_food(n_food, food_size, npp, max_food)
av_food_dist = w.av_food_dist()

# color stuff
cp = plt.get_cmap('Paired')
cnorm = cl.Normalize(vmin=0, vmax=n_hives)
scmap = cm.ScalarMappable(norm=cnorm, cmap=cp)

# plot stuff
fg, ax = plt.subplots(1,n_hives + 2)
ax[1].clear()

t = range(start, stop)
ax[1].plot(t, [2-1/(log(av_food_dist/1)**2) for _ in t],'-',color='k')

for i in range(start, stop):
    w.step()

    if i % 10 == 0:
        hdls = []
        ax[0].clear()
        ax[0].set_aspect('equal')
        ax[0].axis([0, size, 0, size])
        ax[0].imshow(w.grid.T, cmap='Greens', vmin=0, vmax=max_food, \
                interpolation='nearest')

        for j in range(len(w.hives)):
            hive = w.hives[j]
            bees = hive.bees

            ax[0].plot(hive.x, hive.y, 'rd')
            ax[0].scatter([b.x for b in bees], [b.y for b in bees], \
                    cmap = 'Paired', vmin=0, vmax=n_hives, \
                    c=[j for _ in range(len(bees))])

            mus = [b.mu for b in hive.bees]
            cval = scmap.to_rgba(j)
            h, = ax[1].plot(i, np.mean(mus), '.', \
                    color=cval, label = l_labels[j])
            hdls.append(h)
            ax[1].set_aspect((i+1-start)/2.)
            ax[1].axis([start, i+1, 1, 3])

            ax[2+j].clear()
            n, bins, patches = ax[2+j].hist(mus,normed=True, color=cval)
            ax[2+j].axis([1, 3, min(n), max(n)])
            ax[2+j].set_aspect(2.\
                    /float(max(n)-min(n)))
        plt.legend(handles = hdls, loc = 3, bbox_to_anchor=(0., 1.02, 1., .102), mode = 'expand')
        plt.draw()
        plt.pause(0.1)


