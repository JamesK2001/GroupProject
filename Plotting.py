# -*- coding: utf-8 -*-
"""
Created on Mon May 10 15:51:02 2021

@author: kerrj
"""

import numpy as np
import matplotlib.pyplot as plt
import Simulator 
import easygui
Simu = Simulator.Simulation()

#Setting up the graph
plt.xlabel("Time/days")
plt.ylabel("Number (1000s)")
plt.grid()

#Setting up the GUI
question = "Please select desired plots for graph."
title = "Options for Plotting"
listofoptions = ["Suseptible", "Exposed", "Asymptomatic", "Symptomatic", "Self-Isolating", "Hospitalised", "Dead", "Recovered"]

#Launching the GUI with all the options
choice = easygui.multchoicebox(question, title, listofoptions)


#Plotting given options
for i in choice:
    if i == "Suseptible":
        plt.plot(Simu.S, label="Suseptible")
    if i == "Exposed":
        plt.plot(Simu.E, label="Exposed")
    if i == "Asymptomatic":
        plt.plot(Simu.Asymp, label="Asymptomatic")
    if i == "Symptomatic":
        plt.plot(Simu.Symp, label="Symptomatic")
    if i == "Self-Isolating":
        plt.plot(Simu.Iso, label="Self-Isolating")
    if i == "Hospitalised":
        plt.plot(Simu.Hos, label="Hospitalised")
    if i == "Dead":
        plt.plot(Simu.D, label="Dead")
    if i == "Recovered":
        plt.plot(Simu.R, label="Recovered")

#Adding a key to the graph        
plt.legend()

