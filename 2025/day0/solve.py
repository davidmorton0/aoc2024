#!/usr/bin/env python
import time

class Solve:
    def __init__(self):
        self.values = []

    def load_input(self, filename):
        with open(filename, 'r') as file:
            input = file.read().split("\n")
            return input


    def solve_a(self, filename):
        input = self.load_input(filename)

    def solve_b(self, filename):
        input = self.load_input(filename)





start_time = time.time()
Solve().solve_a('example.txt')
# Solve().solve_a('input.txt')
print("\n")
# Solve().solve_b('example.txt')
# Solve().solve_b('input.txt')
print("--- %s seconds ---" % (time.time() - start_time))