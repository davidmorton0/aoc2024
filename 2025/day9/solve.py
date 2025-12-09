#!/usr/bin/env python
import time

class Solve:
    def __init__(self):
        self.values = []

    def load_input(self, filename):
        with open(filename, 'r') as file:
            input = file.read().split("\n")
            coordinates = []
            for line in input:
                coordinates.append([int(coordinate) for coordinate in line.split(",")])
            return coordinates


    def solve_a(self, filename):
        coordinates = self.load_input(filename)
        print(coordinates)
        self.calculate_largest_area(coordinates)
    
    def calculate_largest_area(self, coordinates):
        highest = [0]
        for n, [x1, y1] in enumerate(coordinates):
            for m, [x2, y2] in enumerate(coordinates):
                area = ((abs(x1 - x2) + 1) * (abs(y1 - y2) + 1))
                if area > highest[0]:
                    highest = [area, [x1, y1], [x2, y2]]
        print(highest)
                

    def solve_b(self, filename):
        input = self.load_input(filename)





start_time = time.time()
Solve().solve_a('example.txt')
Solve().solve_a('input.txt')
print("\n")
# Solve().solve_b('example.txt')
# Solve().solve_b('input.txt')
print("--- %s seconds ---" % (time.time() - start_time))