#!/usr/bin/env python
import time
from math import floor
from re import split

class Solve:
    def __init__(self):
        self.ingredients = []
        self.ingredients_ranges = []

    def load_input(self, filename):
        with (open(filename, 'r') as file):
            input = file.read().split("\n\n")
            self.ingredients_ranges = [[int(j) for j in i.split("-")] for i in input[0].split("\n")]
            self.ingredients = [int(j) for j in input[1].split("\n")]

    def solve_a(self, filename):
        self.load_input(filename)
        fresh_ingredients = 0
        for ingredient in self.ingredients:
            if self.check_ingredient(ingredient):
                fresh_ingredients += 1
        print(fresh_ingredients)


    def check_ingredient(self, ingredient):
        for min, max in self.ingredients_ranges:
            if ingredient >= min and ingredient <= max:
                return True
        return False




    def solve_b(self, filename):
        self.load_input(filename)
        while self.check_ingredients_range():
            print(self.ingredients_ranges)
        print(sum([(y + 1) - x for x, y in self.ingredients_ranges]))



    def check_ingredients_range(self):
        for n, [range_start, range_end] in enumerate(self.ingredients_ranges):
            for m, [check_range_start, check_range_end] in enumerate(self.ingredients_ranges):
                if n != m and ((range_start >= check_range_start and range_start <= check_range_end) or (range_end >= check_range_start and range_end <= check_range_end)):
                    print([range_start, range_end], [check_range_start, check_range_end])
                    self.ingredients_ranges[n] = [min(range_start, check_range_start), max(range_end, check_range_end)]
                    self.ingredients_ranges.pop(m)
                    return True
        return False



start_time = time.time()
# Solve().solve_a('example.txt')
# Solve().solve_a('input.txt')
print("\n")
# Solve().solve_b('example.txt')
Solve().solve_b('input.txt')
print("--- %s seconds ---" % (time.time() - start_time))