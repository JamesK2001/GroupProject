#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May  7 14:48:14 2021

@author: conradodriscoll
"""


import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import odeint
import Simulator
Simu = Simulator.Simulation(948, 10, 10, 10, 15, 5, 1, 1, 1000, 5, 7, 2, 1, 0.2, 0.3, 0.3, 0.1, 0.1, 0.08, 0.1, 0.05, 100)





class Plotter:
    
    def __init__(self):
        
        self.fig = plt.figure(facecolor='w')
        self.ax = self.fig.add_subplot(111, facecolor='#dddddd', axisbelow=True)
        self.ax.set_xlabel('Time /days')
        self.ax.set_ylabel('Number (1000s)')
        self.ax.set_ylim(0,1.2)
        self.ax.yaxis.set_tick_params(length=0)
        self.ax.xaxis.set_tick_params(length=0)
        self.ax.grid(b=True, which='major', c='w', lw=2, ls='-')
        for spine in ('top', 'right', 'bottom', 'left'):
            self.ax.spines[spine].set_visible(False)


    def AddPlot(self, arraytoplot, colourcode, legendlabel):
        
        self.ax.plot(Simu.t, arraytoplot / 1000, colourcode, alpha=0.5, lw=2, label=legendlabel)
        legend = self.ax.legend()
        legend.get_frame().set_alpha(0.5)
        
        






Plotter.AddPlot(Plotter(), Simu.S, 'b', 'Susceptible')
Plotter.AddPlot(Plotter(), Simu.E, 'y', 'Exposed')


#Plot(Simu.S, 'b', 'Suceptible' )

'''


def CreateGraph():
    fig = plt.figure(facecolor='w')
    ax = fig.add_subplot(111, facecolor='#dddddd', axisbelow=True)
#    ax.plot(Simu.t, arraytoplot / 1000, 'b', alpha=0.5, lw=2, label='Susceptible')
    ax.set_xlabel('Time /days')
    ax.set_ylabel('Number (1000s)')
    ax.set_ylim(0,1.2)
    ax.yaxis.set_tick_params(length=0)
    ax.xaxis.set_tick_params(length=0)
    ax.grid(b=True, which='major', c='w', lw=2, ls='-')
    legend = ax.legend()
    legend.get_frame().set_alpha(0.5)
    for spine in ('top', 'right', 'bottom', 'left'):
        ax.spines[spine].set_visible(False)
    plt.show()

def AddPlotts(arraytoplot, colourcode, label):
    fig = plt.figure(facecolor='w')
    ax = fig.add_subplot(111, facecolor='#dddddd', axisbelow=True)
    ax.plot(Simu.t, arraytoplot / 1000, colourcode, alpha=0.5, lw=2, label=label)
    plt.show
    
   '''

