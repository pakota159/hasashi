#!/usr/bin/env python3

import sys

# Setup input and output arguments
in_fname = "input/" + sys.argv[1] if len(sys.argv) == 2 else False
out_fname = "output/" + sys.argv[2] if len(sys.argv) == 3 else False

# Read input
if in_fname:
    with open(in_fname) as f:
        for line in f:
            # Split line
            number_in_line = line.split()

# Write output
if out_fname:
    with open(out_fname, 'w') as out:
        out.write("x")
