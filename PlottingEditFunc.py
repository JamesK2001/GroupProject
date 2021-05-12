# -*- coding: utf-8 -*-
"""
Created on Tue May  4 19:55:13 2021

@author: kerrj
"""

'''
Plotting Functions
Inputs:
    Simulation Class --> Takes the result arrays of the specified states 
    from the attributes of the simulation class.
    Also takes the line space relating to the time duration of the simulation
    
Returns:
    MatPlot graph of simulation with user selected subplots
    to be used in show and/or save to file in runsim.py
    
'''

import matplotlib.pyplot as plt

import easygui


question = "Please select desired plots for graph."#Formatting the GUI checklist
title = "Options for Plotting"

    
def basicplot(Simu):
    plt.xlabel("Time/days")#Creating the graph
    plt.ylabel("Number (1000s)")
    plt.grid()
    

    listofoptions = ["Suseptible", "Infected", "Recovered"]#Options for GUI checklist
    choice = easygui.multchoicebox(question, title, listofoptions)#Launches GUI with options
    for i in choice:#Plots the chosen options on graph
        if i == "Suseptible":
            plt.plot(Simu.t, Simu.S, label="Suseptible")
        if i == "Infected":
            plt.plot(Simu.t, Simu.I, label="Infected")
        if i == "Recovered":
            plt.plot(Simu.t, Simu.R, label="Recovered")
            
    plt.legend()#Adds a key to the graph
                
                
#Same as basic function but includes the additional states for the advanced simulation
def advancedplot(Simu):
    plt.xlabel("Time/days")
    plt.ylabel("Number (1000s)")
    plt.grid()
    
    
    listofoptions = ["Suseptible", "Exposed", "Asymptomatic", "Symptomatic", "Self-Isolating", "Hospitalised", "Dead", "Recovered"]
    choice = easygui.multchoicebox(question, title, listofoptions)
    for i in choice:
        if i == "Suseptible":
            plt.plot(Simu.t, Simu.S, label="Suseptible")
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
    
