# -*- coding: utf-8 -*-
"""
Created on Mon May 10 15:51:02 2021

@author: kerrj
"""

import numpy as np
import matplotlib.pyplot as plt
import Simulator
import easygui
Simu = Simulator.Simulation(948, 10, 10, 10, 15, 5, 1, 1, 1000, 5, 7, 2, 1, 0.2, 0.3, 0.3, 0.1, 0.1, 0.08, 0.1, 0.05, 100)

plt.xlabel("Time/days")
plt.ylabel("Number (1000s)")
plt.grid()

question = "Please select desired plots for graph."
title = "Options for Plotting"
listofoptions = ["Suseptible", "Exposed", "Asymptomatic", "Symptomatic", "Self-Isolating", "Hospitalised", "Dead", "Recovered"]

choice = easygui.multchoicebox(question, title, listofoptions)

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

plt.legend()

