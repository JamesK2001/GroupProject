#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May  7 14:05:38 2021

@author: conradodriscoll
"""
import numpy as np
from scipy.integrate import odeint



class BasicSimulation:
    def __init__(self, inputarray):
        self.inputarray = inputarray
        self.S0 = self.inputarray[0]
        self.I0 = self.inputarray[1]
        self.R0 = self.inputarray[2]
        self.N = self.inputarray[3]
        self.beta = self.inputarray[4]
        self.gamma = self.inputarray[5]
        self.duration = self.inputarray[6]
        self.t = np.linspace(0, int(self.duration), int(self.duration))
        self.arrays = []
        self.S = []
        self.I = []
        self.R = []
    def basicderiv(self, y, t):
        
        S, I, R = y
        dSdt = -self.beta * S * I / self.N
        dIdt = self.beta * S * I / self.N - self.gamma * I
        dRdt = self.gamma * I
        return dSdt, dIdt, dRdt
    
    def basicintegrate(self):
        y0 = self.S0, self.I0, self.R0
        
        ret = odeint(self.basicderiv, y0, self.t)
       
        
        S, I, R = ret.T
        self.arrays = ret.T
        self.S = self.arrays[0]
        self.I = self.arrays[1]
        self.R = self.arrays[2]
        
        



class AdvancedSimulation:
    
    
    
    ''' Class containing the functions to define the derivative equations for the number of people in each state.
    and the function integrate the derivative equations across the time period of the simulation defined as duration.
    Taking inputs of all initial conditions and the constants associated with the simulation. See docstrings for
    more info on what each cosntant etc is related to. Outputs a collection of arrays as well as the individual arrays
    for each state. These arrays can be used for the plotting functions by calling the relevant array.
        '''
    
    def __init__(self, inputarray):
        self.inputarray = inputarray
        self.S0 = self.inputarray[0]
        self.E0 = self.inputarray[1]
        self.Asymp0 = self.inputarray[2]
        self.Symp0 = self.inputarray[3]
        self.Iso0 = self.inputarray[4]
        self.Hos0 = self.inputarray[5]
        self.D0 = self.inputarray[6]
        self.R0 = self.inputarray[7]
        self.N = self.inputarray[8]
        self.a = self.inputarray[9]
        self.b = self.inputarray[10]
        self.c = self.inputarray[11]
        self.f = self.inputarray[12]
        self.g = self.inputarray[13]
        self.j = self.inputarray[14]
        self.L = self.inputarray[15]
        self.m = self.inputarray[16]
        self.p = self.inputarray[17]
        self.q = self.inputarray[18]
        self.u = self.inputarray[19]
        self.v = self.inputarray[20]
        self.duration = self.inputarray[21]
        self.t = np.linspace(0, int(self.duration), int(self.duration))   
        self.arrays = []
        self.S = []
        self.E = []
        self.Asymp = []
        self.Symp = []
        self.Iso = []
        self.Hos = []
        self.D = []
        self.R = []
       
            
    def deriv(self, y, t):
        
        
        ''' Derivative equation function. Defines the ODEs which determine the
        time rate of change in the number of people in each state. Uses the constants defined
        when calling the class.
        '''
        S, E, Asymp, Symp, Iso, Hos, D, R = y
        dSdt = -((S / (self.N - D)) * ((self.a * Asymp) + (self.b * Symp) + (self.c * Iso) + (self.f * Hos)))
        dEdt = (dSdt * -1) - (E * (self.g + self.j))
        dAsympdt = (E * self.g) - (Asymp * self.q)
        dSympdt = (E * self.j) - (Symp * self.L)
        dIsodt = (Symp * self.L) - (Iso * (self.m + self.u))
        dHosdt = (Iso * self.m) - (Hos * (self.v + self.p))
        dDdt = Hos * self.p
        dRdt = (Asymp * self.q) + (Iso * self.u) + (Hos * self.v)
        return dSdt, dEdt, dAsympdt, dSympdt, dIsodt, dHosdt, dDdt, dRdt
            
    def integrate(self):
        ''' Integration Function. Integrates the ODE equations defined in the deriv function
        across the time space defined by the duration of the simulation. Produces an array containing
        all the arrays for each State. Also updates the class attributes for the arrays for 
        the individual states. The contents of the arrays are the values of each
        state at the time intervals throughout the duration of the simulation.
        These time intervals are currently hardcoded to be 1 day
        
        '''
        
        y0 = self.S0, self.E0, self.Asymp0, self.Symp0, self.Iso0, self.Hos0, self.D0, self.R0
        
        ret = odeint(self.deriv, y0, self.t)
       
        
        S, E, Asymp, Symp, Iso, Hos, D, R = ret.T
        
        self.arrays = ret.T
        self.S = self.arrays[0]
        self.E = self.arrays[1]
        self.Asymp = self.arrays[2]
        self.Symp = self.arrays[3]
        self.Iso = self.arrays[4]
        self.Hos = self.arrays[5]
        self.D = self.arrays[6]
        self.R = self.arrays[7]
       
        
  

