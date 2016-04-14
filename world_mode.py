#!/usr/bin/env python

# import project classes
from food import *
from hive_mode import *
from hive_speed import *

# import other classes
from random import random as rand
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as cl
import matplotlib.cm as cm

class World:
    def __init__(self, size):
        self.size = size
        self.grid = np.zeros([size, size])
        self.hives = []
        self.food = []

    def create_hive_mode(self, n_hives, n_bees):
        # create hives x,y, n_bees, size, grid
        for _ in range(int(n_hives)):
            self.hives.append(HiveMode(int(rand()*self.size), int(rand()*self.size),\
                n_bees, size, self.grid))

    def create_hive_speed(self, n_hives, n_bees):
        for _ in range(n_hives):
            self.hives.append(HiveSpeed(int(rand()*self.size), int(rand()*self.size),\
                n_bees, size, self.grid))

    def create_hive(self, n_hives, n_bees):
        for _ in range(int(n_hives)):
            self.hives.append(Hive(int(rand()*self.size), int(rand()*self.size),\
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

size = 100
n_food = 7
food_size = 6
npp = 0.01
max_food = 1.1

tot_n_bees = 100
n_hives = 2
n_bees = int(tot_n_bees/n_hives)

w1 = World(size)
w2 = World(size)
start = 0
stop = 100000

w1.create_hive_mode(int(n_hives)/2, n_bees)
w2.create_hive(int(n_hives)/2, n_bees) # speedy levy walk (blind)
w1.create_food(n_food, food_size, npp, max_food)
w2.create_food(n_food, food_size, npp, max_food)

l_labels = ['Moding bees', 'Levy Bees']

# color stuff
cp = plt.get_cmap('Paired')
cnorm = cl.Normalize(vmin=0, vmax=n_hives)
scmap = cm.ScalarMappable(norm=cnorm, cmap=cp)

# plot stuff
fg, ax = plt.subplots(3,n_hives)
#ax[0][1].clear()
#ax[0][1].set_title('Mean of mu')

for i in range(start, stop):
    w1.step()
    w2.step()

    if i % 10 == 0:
        hdls = []
        ax[0][0].clear()
        ax[0][0].set_title('Watch the modeing bees!')
        ax[0][0].set_aspect('equal')
        ax[0][0].axis([0, size, 0, size])
        ax[0][0].imshow(w1.grid.T, cmap='Greens', vmin=0, vmax=max_food, \
                interpolation='nearest')

        ax[0][1].clear()
        ax[0][1].set_title('Watch the levy bees!')
        ax[0][1].set_aspect('equal')
        ax[0][1].axis([0, size, 0, size])
        ax[0][1].imshow(w2.grid.T, cmap='Greens', vmin=0, vmax=max_food, \
                interpolation='nearest')
        hives = [w1.hives[0], w2.hives[0]]
        for j in range(2):
            hive = hives[j]
            bees = hive.bees

            ax[0][j].plot(hive.x, hive.y, 'ys')
            ax[0][j].scatter([b.x for b in bees], [b.y for b in bees], \
                    cmap = 'Paired', vmin=0, vmax=n_hives, \
                    c=[j for _ in range(len(bees))])

            mus = [b.mu for b in hive.bees]
            dists = [d[0] for d in hive.travel_dists]

            cval = scmap.to_rgba(j)
            #h, = ax[0][0].plot(i, np.mean(mus), '.', \
                    #color=cval, label = l_labels[j])

            #hdls.append(h)
            #ax[0][1].set_aspect((i+1-start)/100.)
            #ax[0][1].axis([start, i+1, 0, 100])

            ax[1][j].clear()
            ax[1][j].set_title('mu histogram')
            n, bins, patches = ax[1][j].hist(mus,normed=True, color=cval)
            ax[1][j].axis([min(bins), max(bins), min(n), max(n)])
            ax[1][j].set_aspect(float(max(bins)-min(bins))\
                    /float(max(n)-min(n)))

            if len(dists) > 0:
                ax[2][j].clear()
                ax[2][j].set_title('dist histogram')
                n, bins, patches = ax[2][j].hist(dists,normed=True, color=cval)
                ax[2][j].axis([min(bins), max(bins), min(n), max(n)])
                ax[2][j].set_aspect(float(max(bins)-min(bins))\
                        /float(max(n)-min(n)))

        plt.draw()
        plt.pause(0.1)


