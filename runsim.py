#!/usr/bin/env python3
"""

simulator.py
FCP Group Project
May 2021

This script runs simulations of an epidemic (e.g. coronavirus) using ODEs which
define the rate of change in the number of people in each epidemic state. The
rates of transition between states are determined by the constants the user 
inputs which are related to properties of a virus/infection.
There are two versions of the Simulation, Basic and Advanced.
Basic Version is modelled on the SIR model with 3 states.
The Advanced version is a model built upon the SIR model with more DEs in a 
system  constructed by Conrad with more states (insert number of states)
in order to reflect the coronavirus pandemic more specifically. 
The construction of the model and its relevant paramaters can be found in the report.
  
The script can be used to:
    1. Select a version of the simulation to perform
    2. Enter the relevant parameters and constants via command line interface
    3. Show a plotted graph of the simulation on screen (With the plots
        selected by the user via a GUI)
    4. Save an image of the graph produced by the simulation to a file
    5. Save a text file containing brief descriptions of the parameters
        and the value of these parameters input by the user for their simulation
        


    In Order to use the GUI for the graph plotting selection, you must have 
    easy gui installed ( Does not work on Apple/Mac OSX ): Input instructions?
    
    Usage:
        $ python runsim.py --version=('Basic' or 'Advanced') --graph --graphfile --constants --constantsfile
        --version : Select 'Basic' or 'Advanced' 
        (Inputs other than this will return error message and end the program. No input = default = 'Basic'
        --graph : to produce plots include --graph in command line argument
        --graphfile : filename to save an image of the graph to
        --constants : to save a txt file of the inputs for the simulation include --constants in command line argument
        --constantsfile : if --constants , you must input the desired filename as --constantsfile='filename.txt'
    All Saved Files can be found in the directory in which the program resides in
    
"""

import argparse
import FinalSimulator as Simulator
import inputhandler 
import FinalPlottingFunc as FPF
import WriteToResultsFile as WTRF


def main(*args):
    """
    CLI ENTRY POINT
    """
    parser = argparse.ArgumentParser(description='Simulate an epidemic')


    parser.add_argument('--version', metavar='V', type=str, default='Basic',
                        help='Choice of "Basic" SIR simulator or "Advanced" Simulator with more states')
                                
    parser.add_argument('--graph', action='store_true',
                        help='Plot Results on a graph')

    parser.add_argument('--graphfile', metavar='GF', type=str, default=None,
                        help=' Filename to save Graph to')
    parser.add_argument('--constants', action='store_true',
                        help='Record and Save Simulation inputs to a txt file?')
    parser.add_argument('--constantsfile', metavar='CF', type=str, default=None,
                        help=' Filename to save Constants Text File to')
    args = parser.parse_args(args)
    
    
# Handling Version argument input and requesting version specifc inputs:
    
    
    userversion = args.version
    
    userinput = inputhandler.InputHandler(userversion)
   


# Setting up simulation depending on Version selected 

 ## Basic Version Path  
    if userinput.version == "Basic":
        basicsim = Simulator.BasicSimulation(userinput.basicinputarray)
            
        if args.graph:

            fig = FPF.basicplot(basicsim)
            if args.graphfile is None:
                fig.show()
            else:
                fig.show()
                fig.savefig(args.graphfile)
        if args.constants:
            WTRF.ConstantstoFile(args.constantsfile, userinput.basicinputarray)
            
        
        
                
            
            
            
            
## Advanced Version Path
    
    if userinput.version == "Advanced":

        advancedsim = Simulator.AdvancedSimulation(userinput.advancedinputarray)
        
        if args.graph:
            fig = FPF.advancedplot(advancedsim)
            if args.graphfile is None:
                fig.show()
            else:
                fig.show()
                fig.savefig(args.graphfile)
        if args.constants:
            WTRF.ConstantstoFile(args.constantsfile, userinput.advancedinputarray)
            
        
      
    else:
        print("Simulation Complete")
        
        exit()
        

        
    

if __name__ == "__main__":
    #
    # CLI entry point.
    #
    import sys
    main(*sys.argv[1:])
