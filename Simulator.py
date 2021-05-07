#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May  7 14:05:38 2021

@author: conradodriscoll
"""
import numpy as np
from scipy.integrate import odeint





class Simulation:
    
    
    
    ''' Class containing the functions to define the derivative equations for the number of people in each state.
    and the function integrate the derivative equations across the time period of the simulation defined as duration.
    Taking inputs of all initial conditions and the constants associated with the simulation. See docstrings for
    more info on what each cosntant etc is related to. Outputs a collection of arrays as well as the individual arrays
    for each state. These arrays can be used for the plotting functions by calling the relevant array.
        '''
    
    def __init__(self, S0, E0, Asymp0, Symp0, Iso0, Hos0, D0, R0, N, a, b, c, f, g, j, L, m, p, q, u, v, duration):
        self.S0 = S0
        self.E0 = E0
        self.Asymp0 = Asymp0
        self.Symp0 = Symp0
        self.Iso0 = Iso0
        self.Hos0 = Hos0
        self.D0 = D0
        self.R0 = R0
        self.N = N
        self.a = a
        self.b = b
        self.c = c
        self.f = f
        self.g = g
        self.j = j
        self.L = L
        self.m = m
        self.p = p
        self.q = q
        self.u = u
        self.v = v
        self.duration = duration
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
       
        
  

