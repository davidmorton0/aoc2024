#!/usr/bin/env python
import time
from math import floor
from re import split

class Solve:
    def __init__(self):
        self.dial_position = 50
        self.passed_zeros = 0

    def load_input(self, filename):
        with open(filename, 'r') as file:
            return [line for line in file.read().split("\n") if line != ""]

    def solve_a(self, filename):
        number_of_zeros_landed_on = 0
        for line in self.load_input(filename):
            direction, number = line[0], line[1:]
            self.turn_dial(direction, number)
            if self.dial_position == 0:
                number_of_zeros_landed_on += 1

        print("\n", f"{number_of_zeros_landed_on}")

    def solve_b(self, filename):
        zeros_passed = 0
        for line in self.load_input(filename):
            direction, number = line[0], line[1:]
            result = self.turn_dial(direction, number)
            finish = result["finish"]
            if direction == "R":
                zeros_passed += floor(finish / 100)
            elif direction == "L":
                if result["start"] == 0:
                    zeros_passed += abs(floor(finish / 100)) - 1
                else:
                    zeros_passed += abs(floor((finish - 1) / 100))
            # print(f"{result["start"]}, {direction}{number}, {finish}, {self.dial_position} {zeros_passed}")

        print(zeros_passed)

    def turn_dial(self, direction, number):
        start = self.dial_position
        finish = 0
        if direction == "L":
            finish = start - int(number)
        elif direction == "R":
            finish = start + int(number)
        self.dial_position = finish % 100
        return {
            "start": start,
            "finish": finish
        }

start_time = time.time()
Solve().solve_a('example.txt')
Solve().solve_a('input.txt')
print("\n")
Solve().solve_b('example.txt')
Solve().solve_b('input.txt')
print("--- %s seconds ---" % (time.time() - start_time))