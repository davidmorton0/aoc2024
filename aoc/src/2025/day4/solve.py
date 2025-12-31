#!/usr/bin/env python
import time
from math import floor
from re import split

class Solve:
    def __init__(self):
        self.accessible_rolls = 0
        self.total_rolls_removed = 0
        self.grid = []
        self.grid_width = None
        self.grid_height = None

    def load_input(self, filename):
        with open(filename, 'r') as file:
            lines = [line for line in file.read().split("\n") if line != ""]
            for line in lines:
                self.grid.append(list(line))
            self.grid_width = len(self.grid[0])
            self.grid_height = len(self.grid)


    def solve_a(self, filename):
        self.load_input(filename)
        accesible_rolls = 0
        for y, _ in enumerate(self.grid):
            for x, _ in enumerate(self.grid):
                if self.is_roll(x, y) and self.is_roll_accessible(x, y):
                    accesible_rolls += 1
        print(accesible_rolls)

    def solve_b(self, filename):
        self.load_input(filename)
        while self.remove_rolls() > 0:
            print(self.total_rolls_removed)

    def remove_rolls(self):
        rolls_removed = 0
        for y, _ in enumerate(self.grid):
            for x, _ in enumerate(self.grid):
                if self.is_roll(x, y) and self.is_roll_accessible(x, y):
                    self.grid[y][x] = "."
                    rolls_removed += 1
                    self.total_rolls_removed += 1
        return rolls_removed


    def is_roll(self, x, y):
        return self.grid[y][x] == "@"


    def is_roll_accessible(self, x, y):
        # print("checking", [x, y])
        places_to_check = [
            [x + 1, y + 1],
            [x, y + 1],
            [x - 1, y + 1],
            [x + 1, y],
            [x - 1, y],
            [x + 1, y - 1],
            [x, y - 1],
            [x - 1, y - 1],
        ]
        nearby_rolls = 0
        # print(places_to_check)
        for check_x, check_y in places_to_check:
            if check_x >= 0 and check_x < self.grid_width and check_y >= 0 and check_y < self.grid_height:
                # print("checking for roll in", [check_x, check_y])
                if self.grid[check_y][check_x] == "@":
                    nearby_rolls += 1
                    # print(nearby_rolls)
                    if nearby_rolls >= 4:
                        # print("not accessible")
                        return False
        # print("accessible")
        return True


start_time = time.time()
# Solve().solve_a('example.txt')
# Solve().solve_a('input.txt')
print("\n")
Solve().solve_b('example.txt')
Solve().solve_b('input.txt')
print("--- %s seconds ---" % (time.time() - start_time))