#!/usr/bin/env python3

"""
Main frame for Pathogen Simulator

"""

import argparse
import Simulator

def main(*args):
    """
    Command Line Entry Point.
    
    
    
    
    
    """
    parser = argparse.ArgumentParser(description='Simulate an epidemic')
    
    
    parser.add_argument('--duration', metavar='T', type=int, default=100,
                        help='Simulate for T days')
    parser.add_argument('--AsympC', metavar='a', type=int, default=5,
                        help='Asymptomatice Number of Contacts (per day)')
    parser.add_argument('--SympC', metavar='b', type=int, default=7,
                        help='Symptomatic Number of Contacts (per day)')
    parser.add_argument('--IsoC', metavar='c', type=int, default=2,
                        help='Self Isolated Number of Contacts(per day)')
    parser.add_argument('--HosC', metavar='f', type=int, default=1,
                        help='Hospitalised Number of Contacts(per day)')

    parser.add_argument('--EAsymp', metavar='g', type=float, default=0.2,
                        help='Probability of Exposed Person becoming \
                            Asymptomatic Infected (per day)')
    parser.add_argument('--ESymp', metavar='j', type=float, default=0.3,
                        help='Probability of Exposed Person becoming \
                            Symptomatic Infected (per day)')
    parser.add_argument('--SympIso', metavar='L', type=float, default=0.3,
                        help='Probability that a Symptomatic person will \
                            self isolate (per day)') 
    parser.add_argument('--IsoHos', metavar='m', type=float, default=0.1,
                        help='Probability that a Self Isolated person will\
                            become hospitalised (per day)')
    parser.add_argument('--HosD', metavar='p', type=float, default=0.1,
                        help='Probability that a Hospitalised Patient\
                            will die (per day)')
    parser.add_argument('--AsympR', metavar='q', type=float, default=0.08,
                        help='Probability that an Asymptomatic person\
                        will recover (per day)')
    parser.add_argument('--IsoR', metavar='u', type=float, default=0.1,
                        help='Probability that a Self Isolated person\
                            will recover (per day)')
    parser.add_argument('--HosR', metavar='v', type=float, default=0.05,
                        help='Probability that a Hospitalised Patient Will\
                            Recover Number (per day)')
 
    
    parser.add_argument('--TotalPopulation', metavar='N', type=int, default=1000,
                        help='Total number of people to Simulate')
    parser.add_argument('--S0', metavar='S0', type=int, default=900,
                        help='Initial Number of Susceptibles')
    parser.add_argument('--E0', metavar='E0', type=int, default=40,
                        help='Initial Number of Exposed')
    parser.add_argument('--Asymp0', metavar='Asymp0', type=int, default=15,
                        help='Initial Number of Asymptomatic Infecteds')
    parser.add_argument('--Symp0', metavar='Symp0', type=int, default=15,
                        help='Initial Number of Symptomatic Infecteds')
    parser.add_argument('--Iso0', metavar='Iso0', type=int, default=10,
                        help='Initial Number of Self Isolated Infecteds')
    parser.add_argument('--Hos0', metavar='Hos0', type=int, default=5,
                        help='Initial Number of Hospitalised Infecteds')
    parser.add_argument('--D0', metavar='D0', type=int, default=0,
                        help='Initial Number of Deaths')
    parser.add_argument('--R0', metavar='R0', type=int, default=15,
                        help='Initial Number of Recovered Alive')
  
    
    
    parser.add_argument('--plot', action='store_true',
                        help='Generate plots instead of an animation')
    parser.add_argument('--file', metavar='file', type=str, default=None,
                       help='Filename to save to instead of showing on screen')
    args = parser.parse_args(args)
    
    ''' Add functionality to import constants and initials from a file?'''
    ''' Add Args to select what plots to Show and other args needed for plotting functions'''
    
#Argument Checker:
    ''' 
    Need to check that Probabilities are all < 1
    Further Checks: Sum of EAsymp and ESymp is < 1
    Check that Sum of S0 E0 Asymp0 Symp0 Iso0 Hos0 D0 and R0 = Total Population
'''


##Setup the simulation

    sim = Simulator.Simulation(args.S0, args.E0, args.Asymp0, args.Symp0,\
                                      args.Iso0, args.Hos0, args.D0, args.R0,\
                                    args.TotalPopulation, args.AsympC, args.SympC, args.IsoC, args.HosC,\
                                   args.EAsymp, args.ESymp, args.SympIso, args.IsoHos, args.HosD,\
                                    args.AsympR, args.IsoR, args.HosR, args.duration)
    sim.integrate()
    
    
    ## Plotting Functions and other Data Analysis
    #Ability to add a plot for Hospital Capacity?
    
    ## Saving to file? Saving any stats?
    
    
