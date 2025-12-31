#!/usr/bin/env python
import time
from math import floor
from re import split

class Solve:
    def __init__(self):
        self.invalid_ids = []

    def load_input(self, filename):
        with open(filename, 'r') as file:
            lines = [line for line in file.read().split("\n") if line != ""][0]
            range_strings = lines.split(",")
            id_ranges = []
            for range_string in range_strings:
                first, last = range_string.split("-")
                id_ranges.append([int(first), int(last)])
            return id_ranges


    def solve_a(self, filename):
        id_ranges = self.load_input(filename)
        for id_range in id_ranges:
            for n in range(id_range[0], id_range[1] + 1):
                length = len(str(n))
                if length % 2 == 0:
                    start = str(n)[:int(length/2)]
                    end = str(n)[int(length/2):]
                    if start == end:
                        self.invalid_ids.append(n)
        # print(self.invalid_ids)
        print(sum(self.invalid_ids))



    def solve_b(self, filename):
        id_ranges = self.load_input(filename)
        for id_range in id_ranges:
            for n in range(id_range[0], id_range[1] + 1):
                if self.check_id(n):
                    self.invalid_ids.append(n)
        print(self.invalid_ids)
        print(sum(self.invalid_ids))

    def check_id(self, id):
        length = len(str(id))
        for l in range(2, length + 1):
            if self.is_repeated(id, length, l):
                return True
        return False

    def is_repeated(self, id, length, repeats):
        if length % repeats == 0:
            repeating_string = str(id)[:int(length / repeats)]
            check_string = repeating_string * repeats
            return check_string == str(id)
        return False


start_time = time.time()
# Solve().solve_a('example.txt')
# Solve().solve_a('input.txt')
print("\n")
Solve().solve_b('example.txt')
Solve().solve_b('input.txt')
print("--- %s seconds ---" % (time.time() - start_time))