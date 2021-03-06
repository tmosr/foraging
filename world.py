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
        dist_food =[]
        for i in range(len(self.food)-1):
            f1 = self.food[i]
            for j in range(len(self.food)-1, i, -1):
                f2 = self.food[j]
                if f1.x - f2.x > size/2:
                    x_dist = size-(f1.x-f2.x)
                else:
                    x_dist = f1.x - f2.x

                if f1.y - f2.y > size/2:
                    y_dist = size-(f1.y - f2.y)
                else:
                    y_dist = f1.y - f2.y

                dist_food.append(hypot(x_dist, y_dist))

        afd = np.mean(dist_food)
        return afd

size = 50
n_food = 3
food_size = 2
npp = 0.01
max_food = 1.1

vs = 10
vf = 1

tot_n_bees = 60
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
fg, ax = plt.subplots(2,3)
ax[0][1].clear()

t = range(start, stop)
ax[0][1].set_title('AVG mu')
ax[0][1].plot(t, [2-1/(log(av_food_dist/1)**2) for _ in t],'-',color='k')

for i in range(start, stop):
    w.step()

    if i % 100 == 0:
        hdls = []
        ax[0][0].clear()
        ax[0][0].set_title('Watch the bees!')
        ax[0][0].set_aspect('equal')
        ax[0][0].axis([0, size, 0, size])
        ax[0][0].imshow(w.grid.T, cmap='Greens', vmin=0, vmax=max_food, \
                interpolation='nearest')

        for j in range(len(w.hives)):
            hive = w.hives[j]
            bees = hive.bees

            ax[0][0].plot(hive.x, hive.y, 'rd')
            ax[0][0].scatter([b.x for b in bees], [b.y for b in bees], \
                    cmap = 'Paired', vmin=0, vmax=n_hives, \
                    c=[j for _ in range(len(bees))])

            mus = [b.mu for b in hive.bees]
            cval = scmap.to_rgba(j)
            h, = ax[0][1].plot(i, np.mean(mus), '.', \
                    color=cval, label = l_labels[j])
            hdls.append(h)
            ax[0][1].set_aspect((i+1-start)/2.)
            ax[0][1].axis([start, i+1, 1, 3])


            if len(hive.travel_dists) > 1:
                # dists
                dists = [d[0] for d in hive.travel_dists]
                # mus
                ms = [d[1] for d in hive.travel_dists]

                ax[j][2].clear()
                ax[j][2].set_title('Distance vs. mu')
                ax[j][2].axis([min(ms), max(ms), min(dists), max(dists)])
                ax[j][2].set_aspect(float(max(ms) - min(ms))/\
                        float(max(dists)-min(dists)))
                ax[j][2].scatter(ms, dists, cmap = 'Paired', c=cval)

            ax[1][j].clear()
            ax[1][j].set_title('mu histogramm')
            n, bins, patches = ax[1][j].hist(mus,normed=True, color=cval)
            ax[1][j].axis([1, 3, min(n), max(n)])
            ax[1][j].set_aspect(2.\
                    /float(max(n)-min(n)))

        plt.figlegend(hdls, l_labels, 'upper right')
        plt.draw()
        plt.pause(0.0001)


