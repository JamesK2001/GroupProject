# -*- coding: utf-8 -*-
"""
Created on Tue May 11 15:50:47 2021

@author: GlenA
"""

def ConstantstoFile(filename, inputarray):
    '''
    

    Parameters
    ----------
    filename : .txt format 
    Filename to save the Text file to.
    inputarray : The array of user inputs
    for their simulation.

    Returns
    -------
    A new .txt file containing the user inputs
    for the simulation they have run.
    File name is specified in the command line 
    when running the runsim.py program
    '''
#Determines Version by length of input array:
    # Advanced Version
    if len(inputarray) > 8:
        Susceptible0, Exposed0, Asymptomatic0, Symptomatic0, Self_Isolated0,\
            Hospitilised0, Dead0, Recovered_Alive0, N, AsympC, SympC, IsoC, HosC,\
            EAsymp, ESymp, SympIso, IsoHos, HosD, AsympR, IsoR, HosR, duration = inputarray
        simulationResult_file = open(filename, "w")
        simulationResult_file.write("\nCONSTANTS USED FOR LAST SIMULATION")
        simulationResult_file.write("\nInitial Number of Susceptible Persons: ")
        simulationResult_file.write(str(Susceptible0))
        simulationResult_file.write("\nInitial Number of Exposed Persons: ")
        simulationResult_file.write(str(Exposed0))
        simulationResult_file.write("\nInitial Number of Asymptomatic Persons: ")
        simulationResult_file.write(str(Asymptomatic0))
        simulationResult_file.write("\nInitial Number of Symptomatic Perons: ")
        simulationResult_file.write(str(Symptomatic0))
        simulationResult_file.write("\nInitial Number of Isolated Persons: ")
        simulationResult_file.write(str(Self_Isolated0))
        simulationResult_file.write("\nInitial Number of Hospitilised Persons:")
        simulationResult_file.write(str(Hospitilised0))
        simulationResult_file.write("\nInitial Number of Dead Persons: ")
        simulationResult_file.write(str(Dead0))
        simulationResult_file.write("\nInitial Number of Recovered Persons: ")
        simulationResult_file.write(str(Recovered_Alive0))
        simulationResult_file.write("\nPopulation Within Model: ")
        simulationResult_file.write(str(N))
        simulationResult_file.write("\n>>Contact Implies a Successful Transmission<<")
        simulationResult_file.write("\nNumber of Asymptomatic Contacts per Day: ")
        simulationResult_file.write(str(AsympC))
        simulationResult_file.write("\nNumber of Symptomatic Contacts per Day: ")
        simulationResult_file.write(str(SympC))
        simulationResult_file.write("\nNumber of Isolated Contacts per Day: ")
        simulationResult_file.write(str(IsoC))
        simulationResult_file.write("\nNumber of Hospitilised Contacts per Day: ")
        simulationResult_file.write(str(HosC))
        simulationResult_file.write("\nFraction of Exposed Population to Asymptomatic per Day: ")
        simulationResult_file.write(str(EAsymp))
        simulationResult_file.write("\nFraction of Exposed Population to Symptomatic per Day: ")
        simulationResult_file.write(str(ESymp))
        simulationResult_file.write("\nFraction of Symptomatic Population to Isolated per Day: ")
        simulationResult_file.write(str(SympIso))
        simulationResult_file.write("\nFraaction of Isolated Population to Hospitilised per Day: ")
        simulationResult_file.write(str(IsoHos))
        simulationResult_file.write("\nFraction of Hospitilised Population that Die per Day: ")
        simulationResult_file.write(str(HosD))
        simulationResult_file.write("\nFraction of Asymptomatic Population that Recover per Day: ")
        simulationResult_file.write(str(AsympR))
        simulationResult_file.write("\nFraction of Isolated Population that Recover per Day: ")
        simulationResult_file.write(str(IsoR))
        simulationResult_file.write("\nFraction of Hospitalised Population that Recover per Day: ")
        simulationResult_file.write(str(HosR))
        simulationResult_file.write("\nNumber of Days for Model: ")
        simulationResult_file.write(duration)
        simulationResult_file.close()
# Basic Version        
    if len(inputarray) < 8:
        Susceptible0, Infected0, Recovered0, N, beta, gamma, duration = inputarray
        simulationResult_file = open(filename, "w")
        simulationResult_file.write("\nCONSTANTS USED FOR LAST SIMULATION")
        simulationResult_file.write("\nInitial Number of Susceptible Persons: ")
        simulationResult_file.write(str(Susceptible0))
        simulationResult_file.write("\nInitial Number of Infected Persons: ")
        simulationResult_file.write(str(Infected0))
        simulationResult_file.write("\nInitial Number of Recovered Persons: ")
        simulationResult_file.write(str(Recovered0))
        simulationResult_file.write("\nPopulation Within Model: ")
        simulationResult_file.write(str(N))
        simulationResult_file.write("\nNumber of Infected Contacts sufficient to spread virus per day: ")
        simulationResult_file.write(str(beta))
        simulationResult_file.write("\nRecovery Rate for Infected Population per day: ")
        simulationResult_file.write(str(gamma))
        simulationResult_file.write("\nNumber of Days for Model: ")
        simulationResult_file.write(duration)
        simulationResult_file.close()
        