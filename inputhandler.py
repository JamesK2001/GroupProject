#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Class definiton of the input handling module.
Inputs:
    Simulation Version
Process:
    Requests the necessary input parameters for the simulation version
    from the user whilst giving a brief description of each.
    Holds necessary conditions for these parameters when necessary
Returns:
    A 1D array of the input parameters to be used in simulation module
    and SaveInputsToFile module via the runsim.py program.
    
Created on Mon May 10 17:51:55 2021

@author: conradodriscoll
"""


class InputHandler:
    
    def __init__(self, versioninput):
        self.versioninput = versioninput
        self.version = None
        self.helpmessage = "Invalid --version Input: --version='Basic' or --version='Advanced' depending on simulation version you would like to use"
        self.basicinputarray = []
        self.advancedinputarray = []
        self.handleversion()
        self.run()
        
    def handleversion(self):
        while True:
            try:
                "Basic" == self.versioninput or "Advanced" == self.versioninput
                if True:
                    self.version = self.versioninput
                    return self.version
                else:
                    print("Invalid Command Line Argument for Version")
                    return 
                
            except Exception as e:
                print("Invalid input:", e)
                
    def run(self):
        if self.version == "Basic":
            self.handlebasicinput()
                
        elif self.version == "Advanced":
            self.handleadvancedinput()
        
        else:
            print(self.helpmessage)
      
    
    def handlebasicinput(self):
        
        while True:
            try:
                I0 = int(input("Number of Initially Infected People:"))
                if (I0 >= 0):
                    break
                else:
                    print("Invalid Input, >= 0 ")
            except Exception as e:
                print("Error:", e)
                
        while True:
            try:
                R0 = int(input("Number of Initially Recovered People:"))
                if (R0 >= 0):
                    break
                else:
                    print("Invalid Input, >= 0 ")
            except Exception as e:
                print("Error:", e)
                
        while True:
            try:
                N = int(input("Total Number of People:"))
                if ( N >= (I0 + R0)):
                    break
                else:
                    print("Invalid Input, >= 0 AND Greater than the Sum of I0 + R0")
            except Exception as e:
                print("Error:", e)
        while True:
            try:
                beta = float(input("Number of Contacts by an infected person per day which are Sufficient to spread the disease :"))
                if (beta >= 0):
                    break
                else:
                    print("Invalid Input, >= 0 ")
            except Exception as e:
                print("Error:", e)
        
        while True:
            try:
                gamma = float(input("Recovery rate of Infected People. (I.e 1/number of days it takes to become noninfectious) Equivalent to the fraction of the infected population that recover per day:"))
                            
                if (gamma >= 0 and gamma <= 1):
                    break
                else:
                    print("Invalid Input, 1 >= gamma >= 0 ")
            except Exception as e:
                print("Error:", e)
                
        while True:
            try:
                duration = int(input("Number of days to run the simulation for"))
                if (duration >= 0):
                    break
                else:
                    print("Invalid Input, >= 0 ")
            except Exception as e:
                print("Error:", e)
           
        S0 = N - R0 - I0
        
        *self.basicinputarray, = S0, I0, R0, N, beta, gamma, duration 
    
    
    def handleadvancedinput(self):
        
        
        while True:
            try:
                E0 = int(input("Initial Number of People Exposed to Virus:"))
                if (E0 >= 0):
                    break
                else:
                    print("Invalid Input, >= 0 ")
            except Exception as e:
                print("Error:", e)
        
        while True:
            try:
                Asymp0 = int(input("Initial Number of Asymptomatic Infected People:"))
                if (Asymp0 >= 0):
                    break
                else:
                    print("Invalid Input, >= 0 ")
            except Exception as e:
                print("Error:", e)
                
        while True:
            try:
                Symp0 = int(input("Initial Number of Symptomatic Infected People:"))
                if (Symp0 >= 0):
                    break
                else:
                    print("Invalid Input, >= 0 ")
            except Exception as e:
                print("Error:", e)
        while True:
            try:
                Iso0 = int(input("Initial Number of Self Isolated People ( Chceck ReadMe for info on how this state is define)"))
                if (Iso0 >= 0):
                    break
                else:
                    print("Invalid Input, >= 0 ")
            except Exception as e:
                print("Error:", e)
        while True:
            try:
                Hos0 = int(input("Initial Number of People Hospitalised by the Virus:"))
                if (Hos0 >= 0):
                    break
                else:
                    print("Invalid Input, >= 0 ")
            except Exception as e:
                print("Error:", e)
        while True:
            try:
                D0 = int(input("Initial Number of People Killed by Virus:"))
                if (D0 >= 0):
                    break
                else:
                    print("Invalid Input, >= 0 ")
            except Exception as e:
                print("Error:", e)
        while True:
            try:
                R0 = int(input("Initial Number of People who have recovered from the virus:"))
                if (R0 >= 0):
                    break
                else:
                    print("Invalid Input, >= 0 ")
            except Exception as e:
                print("Error:", e)
        while True:
            try:
                N = int(input("Total Number of People in Simulation ( Total population):"))
                if (N >= 0 and N >= E0 + Asymp0 + Symp0 + Iso0 + Hos0 + D0 + R0 ):
                    break
                else:
                    print("Invalid Input, N >= 0 and N >= Sum of E0, Asymp0, Symp0, Iso0, Hos0, D0, R0 ")
            except Exception as e:
                print("Error:", e)
       
        while True:
            try:
                a = float(input("Number of Contacts sufficient to Spread virus by Asymptomatic Infected Person Per Day"))
                if (a >= 0):
                    break
                else:
                    print("Invalid Input, >= 0 ")
            except Exception as e:
                print("Error:", e)
        while True:
            try:
                b = float(input("Number of Contacts sufficient to Spread virus by Symptomatic Infected Person Per Day"))
                if (b >= 0):
                    break
                else:
                    print("Invalid Input, >= 0 ")
            except Exception as e:
                print("Error:", e)
        while True:
            try:
                c = float(input("Number of Contacts sufficient to Spread virus by Self-Isolated Infected Person Per Day"))
                if (c >= 0):
                    break
                else:
                    print("Invalid Input, >= 0 ")
            except Exception as e:
                print("Error:", e)
                
        while True:
            try:
                f = float(input("Number of Contacts sufficient to Spread virus by Hospitalised Infected Person Per Day"))
                if (f >= 0):
                    break
                else:
                    print("Invalid Input, >= 0 ")
            except Exception as e:
                print("Error:", e)
        
        print( " -- USAGE MESSAGE --- " + "\n" + " The Next Input Relates to the total fraction of the Exposed Population that become infected per day (= k ) . The Input after this relates to the Fraction of the Exposed Population that become Asymptomatic Infected ( = g) . The fraction of the Exposed Population that become Symptomatic Infected per day ( = j )  will be calculated by subtracting 'g' from 'k' . i.e. j = k - g  Therefore g must be less than k and k must be less than or equal to 1 ")
        while True:
            try:
                k = float(input("Fraction of Total Exposed Population that Become Infected Per Day . Equivalent to 1/(Incubation Periods in Days) "))
                if (k >= 0 and k <= 1.0 ):
                    break
                else:
                    print("Invalid Input, 1 >= k >= 0  ")
            except Exception as e:
                print("Error:", e)
        while True:
            try:
                g = float(input("Fraction of Exposed Population that become Asymptomatic Infected Per Day"))
                if (g >= 0 and g <= k):
                    break
                else:
                    print("Invalid Input, k >= g >= 0 " + " Your k Value is: " + str(k))
            except Exception as e:
                print("Error:", e)
                
        j = k - g

        print("Your j value is:" + str(j) + "This means the fraction of the exposed population that become Symptomatic infected per day is:" + str(j))
        
        
        while True:
            try:
                L = float(input("Fraction of Symptomatic Population that becomes Self-Isolated Per Day Equivalent to 1/(Typical Number of Days between Symptom onset and self isolation)"))
                                
                if (L >= 0 and L <= 1):
                    break
                else:
                    print("Invalid Input, 1 >= L >= 0 ")
            except Exception as e:
                print("Error:", e)
                
        while True:
            try:
                m = float(input("Fraction of Self-Isolated Population that become Hospitalised Per Day. Equivalent to the probability of a Self-isolated infected person being admitted to hospital on a given day"))
                                    
                if (m >= 0 and m <= 1):
                    break
                else:
                    print("Invalid Input, 1 >= m >= 0 ")
            except Exception as e:
                print("Error:", e)
                
        while True:
            try:
                p = float(input("Fraction of The Hospitalised Population that Die per day Equivalent to the probabilitity of a hospitalised person dieing on a given day"))
                if (p >= 0 and p <= 1):
                    break
                else:
                    print("Invalid Input, 1 >= p >= 0 ")
            except Exception as e:
                print("Error:", e)
        while True:
            try:
                q = float(input("Fraction of the Asymptomatic Population that Recover Per Day. Equivalent to 1/(Typical Number of Days Asymptomatic Infected):"))
                if (q >= 0 and q <= 1):
                    break
                else:
                    print("Invalid Input,1 >= q >= 0 ")
            except Exception as e:
                print("Error:", e)
        while True:
            try:
                u = float(input("Fraction of the Self Isolated Population that RecoverPer Day. Equivalent to 1/(Typical Number of Days Self Isolated Before Recovery):"))
                if (u >= 0 and u <= 1 - m):
                    break
                else:
                    print("Invalid Input, (1-m) >= u >= 0 " + "Your m value is:" + str(m) + "Therefore u must be less than or equal to" + str((1-m)))
            except Exception as e:
                print("Error:", e)
                
        while True:
            try:
                v = float(input("Fraction of the Hospitalised Population that Recover Per Day. Equivalent to 1/(Typical Number of Days In Hospital until Recovery)"))
                if (v >= 0 and v <= (1 - p)):
                    break
                else:
                    print("Invalid Input, (1-p) >= v >= 0 " + "Your p value is:" + str(p) + "Therefore v must be less than or equal to" + str((1-p)))
                    
            except Exception as e:
                print("Error:", e)
        while True:
          try:
              duration = int(input("Number of days to run the simulation for"))
              if (duration >= 0):
                  break
              else:
                  print("Invalid Input, >= 0 ")
          except Exception as e:
              print("Error:", e)       
            



        S0 = N - (E0 + Asymp0 + Symp0 + Iso0 + Hos0 + D0 + R0)
        
        *self.advancedinputarray, = S0, E0, Asymp0, Symp0, Iso0, Hos0, D0, R0, N, a, b, c, f, g, j, L, m, p, q, u, v, duration
    




