#!/usr/bin/env python3

import sys

from model import Library, Book, Submission

# Setup input, output
if len(sys.argv) == 1:
    in_fname = "input/a_example.txt"
    out_fname = "output/out.txt"
else:
    # Setup input and output arguments
    in_fname = "input/" + sys.argv[1] if len(sys.argv) == 2 else False
    out_fname = "output/" + sys.argv[2] if len(sys.argv) == 3 else False

total_books = None
total_libs = None
total_days = None
book_holder = {}
lib_holder = {}

# Read input
if in_fname:
    with open(in_fname) as f:
        for i, line in enumerate(f):
            # Split line
            number_in_line = line.split()
            if i == 0:
                total_books = int(number_in_line[0])
                total_libs = int(number_in_line[1])
                total_days = int(number_in_line[2])
            elif i == 1:
                for index, j in enumerate(number_in_line):
                    book_holder.update({index: Book(score=j, book_index=index)})
            elif i > 1 and i % 2 == 0:
                lib_index = i // 2 - 1
                lib_holder.update({lib_index: Library(
                    number_of_books=int(number_in_line[0]),
                    sign_up_days=int(number_in_line[1]),
                    books_per_day=int(number_in_line[2])
                )})
            elif i > 1 and i % 2 == 1:
                book_dict = {}
                lib_index = i // 2 - 1
                for book_index in number_in_line:
                    book_dict.update({book_index: book_holder[int(book_index)]})
                lib_holder[lib_index].books = book_dict

for key in lib_holder:
    print(key)
    # print(lib_holder[key])
    print(lib_holder[key].books)


# Solution here
def solve():
    pass


solve()

# Submit
submission = Submission(out_fname)
submission.submit()

