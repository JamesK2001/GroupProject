# -*- coding: utf-8 -*-
"""
Created on Tue May  4 19:55:13 2021

@author: kerrj
"""


import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import odeint
import Simulator
import easygui
Sim=Simulator.BasicSimulation(1, 2, 2, 600, 7, 0.2, 100)
Simu=Simulator.AdvancedSimulation(948, 10, 10, 10, 15, 5, 1, 1, 1000, 5, 7, 2, 1, 0.2, 0.3, 0.3, 0.1, 0.1, 0.08, 0.1, 0.05, 100)

    
def basicplot():
    plt.xlabel("Time/days")#Creating the graph
    plt.ylabel("Number (1000s)")
    plt.grid()
    
    Sim=Simulator.BasicSimulation()
    question = "Please select desired plots for graph."#Formatting the GUI checklist
    title = "Options for Plotting"
    listofoptions = ["Susceptible", "Infected", "Recovered"]#Options for GUI checklist
    choice = easygui.multchoicebox(question, title, listofoptions)#Launches GUI with options
    for i in choice:#Plots the chosen options on graph
        if i == "Susceptible":
            plt.plot(Sim.t, Sim.S, label="Susceptible")
        if i == "Infected":
            plt.plot(Sim.t, Sim.I, label="Infected")
        if i == "Recovered":
            plt.plot(Sim.t, Sim.R, label="Recovered")
            
    plt.legend()#Adds a key to the graph
                
                
#Same as basic function
def advancedplot():
    plt.xlabel("Time/days")
    plt.ylabel("Number (1000s)")
    plt.grid()
    
    Simu=Simulator.AdvancedSimulation()
    question = "Please select desired plots for graph."#Formatting the GUI checklist
    title = "Options for Plotting"
    listofoptions = ["Susceptible", "Exposed", "Asymptomatic", "Symptomatic", "Self-Isolating", "Hospitalised", "Dead", "Recovered"]
    choice = easygui.multchoicebox(question, title, listofoptions)
    for i in choice:
        if i == "Susceptible":
            plt.plot(Simu.t, Simu.S, label="Susceptible")
        if i == "Exposed":
            plt.plot(Simu.t, Simu.E, label="Exposed")
        if i == "Asymptomatic":
            plt.plot(Simu.t, Simu.Asymp, label="Asymptomatic")
        if i == "Symptomatic":
            plt.plot(Simu.t, Simu.Symp, label="Symptomatic")
        if i == "Self-Isolating":
            plt.plot(Simu.t, Simu.Iso, label="Self-Isolating")
        if i == "Hospitalised":
            plt.plot(Simu.t, Simu.Hos, label="Hospitalised")
        if i == "Dead":
            plt.plot(Simu.t, Simu.D, label="Dead")
        if i == "Recovered":
            plt.plot(Simu.t, Simu.R, label="Recovered")
            
    plt.legend()
    
