#!/usr/bin/env python3

"""

Made a new runsim file to add the discussed changes - i.e.:
Command line inputs reduced to asking which version of the simulator the user
would like to run and how they would like the results output ( graphs etc)
Then using input prompts to request user to input value assignment for the
initial state values and transition constants

"""

import argparse
import Simulator

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
