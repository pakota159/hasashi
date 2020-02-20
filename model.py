#!/usr/bin/env python3
class Pizza:
    def __init__(self):
        self.max_number = None
        self.number_of_types = None
        self.slices_each_type = []

    def convert_int(self):
        self.max_number = int(self.max_number)
        self.number_of_types = int(self.number_of_types)
        self.slices_each_type = list(map(lambda i: int(i), self.slices_each_type))


class Submission:
    def __init__(self, out_fname):
        self.out_fname = out_fname if out_fname else "output/out.txt"

    def submit(self):
        # Write output
        if self.out_fname:
            with open(self.out_fname, 'w') as out:
                out.write("x")
