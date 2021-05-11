#!/usr/bin/env python3

"""

Made a new runsim file to add the discussed changes - i.e.:
Command line inputs reduced to asking which version of the simulator the user
would like to run and how they would like the results output ( graphs etc)
Then using input prompts to request user to input value assignment for the
initial state values and transition constants

"""

import argparse
import FinalSimulator as Simulator
import inputhandler 
import PlottingEditFunc as PEF

def main(*args):
    """
    CLI ENTRY POINT
    """
    parser = argparse.ArgumentParser(description='Simulate an epidemic')


    parser.add_argument('--version', metavar='V', type=str, default='Basic',
                        help='Choice of "Basic" SIR simulator or "Advanced" \
                                Simulator with more states')

    parser.add_argument('--graphfile', metavar='GF', type=str, default=None,
                        help=' Filename to save Graph to')
    parser.add_argument('--constantsfile', metavar='CF', type=str, default=None,
                        help=' Filename to save Constant Text File to')
    args = parser.parse_args(args)
    userversion = args.version
    userinput = inputhandler.InputHandler(userversion)
    
    
    
    
    

    
    if userinput.version == "Basic":
        
        basicsim = Simulator.BasicSimulation(userinput.basicinputarray)
            
        PEF.basicplot(basicsim)
            
    
    elif userinput.version == "Advanced":
        advancedsim = Simulator.AdvancedSimulation(userinput.advancedarray)
        
        
    

if __name__ == "__main__":
    #
    # CLI entry point. The main() function can also be imported and called
    # with string arguments.
    #
    import sys
    main(*sys.argv[1:])
