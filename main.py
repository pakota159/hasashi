#!/usr/bin/env python3

import sys
from model import Pizza, Submission

# Setup input, output
if len(sys.argv) == 1:
    in_fname = "input/a_example.in"
    out_fname = "output/out.txt"
else:
    # Setup input and output arguments
    in_fname = "input/" + sys.argv[1] if len(sys.argv) == 2 else False
    out_fname = "output/" + sys.argv[2] if len(sys.argv) == 3 else False

# Create variable/instance to work later
pizza = Pizza()

# Read input
if in_fname:
    with open(in_fname) as f:
        for i, line in enumerate(f):
            # Split line
            number_in_line = line.split()
            if i == 0:
                pizza.max_number = number_in_line[0]
                pizza.number_of_types = number_in_line[1]
            else:
                pizza.slices_each_type = number_in_line

pizza.convert_int()
print(pizza.max_number)
print(pizza.number_of_types)
print(pizza.slices_each_type)

# Submit
submission = Submission(out_fname)
submission.submit()

