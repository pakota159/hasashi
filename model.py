#!/usr/bin/env python3
class Book:
    def __init__(self, score, book_index):
        self.score = score
        self.book_index = book_index


class Library:
    def __init__(self, number_of_books, sign_up_days, books_per_day):
        self.lib_index = None
        self.number_of_books = number_of_books
        self.books = {}
        self.books_per_day = books_per_day
        self.sign_up_days = sign_up_days


class Submission:
    def __init__(self, out_fname):
        self.out_fname = out_fname if out_fname else "output/out.txt"

    def submit(self):
        # Write output
        if self.out_fname:
            with open(self.out_fname, 'w') as out:
                out.write("x")
