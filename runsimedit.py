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

def main(*args):
    """
    CLI ENTRY POINT
    """
    parser = argparse.ArgumentParser(description='Simulate an epidemic')


    parser.add_argument('--version', metavar='V', type=str, default='Basic',
                        help='Choice of "Basic" SIR simulator or "Advanced" \
                                Simulator with more states')

    parser.add_argument('--output', metavar='O', type=str, default='S',
                        help=' Input "S" for onscreen graph or "F" to \
                        save the graph to a directory. or "B" to do both!')

    args = parser.parse_args(args)
    
    userinput = inputhandler(args.version)
    
    userinput()
    
    if userinput.version == "Basic":
        
        basicsim = Simulator.BasicSimulation(userinput.basicinputarray)
        basicsim()
    
    elif userinput.version == "Advanced":
        advancedsim = Simulator.AdvancedSimulation(userinput.advancedarray)
        advancedsim()
        
    

if __name__ == "__main__":
    #
    # CLI entry point. The main() function can also be imported and called
    # with string arguments.
    #
    import sys
    main(*sys.argv[1:])
