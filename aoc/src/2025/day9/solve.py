#!/usr/bin/env python
import time

class Solve:
    def __init__(self):
        self.grid = []

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
        coordinates = self.load_input(filename)
        print(coordinates)
        print("\n")
        rectangles = self.calculate_rectangles(coordinates)
        for rectangle in rectangles:
            if self.valid_rectangle(rectangle, coordinates):
                print(rectangle)
                return
        

    def calculate_rectangles(self, coordinates):
        rectangles = []
        for n, [x1, y1] in enumerate(coordinates):
            for m, [x2, y2] in enumerate(coordinates):
                if n == m:
                    continue
                area = ((abs(x1 - x2) + 1) * (abs(y1 - y2) + 1))
                rectangles.append([[min(x1, x2) + 1, min(y1, y2) + 1], [max(x1, x2) - 1, max(y1, y2) - 1], area])
        rectangles.sort(key=lambda r : -r[2])
        return rectangles
    
    def valid_rectangle(self, rectangle, coordinates):
        for n in range(0, len(coordinates)):
            x1, y1 = coordinates[n - 1]
            x2, y2 = coordinates[n]
            if self.point_in_rectangle(x1, y1, rectangle) or self.point_in_rectangle(x2, y2, rectangle):
                return False
            if self.line_crosses_rectangle(x1, y1, x2, y2, rectangle):
                return False
        return True
    
    def point_in_rectangle(self, x, y, rectangle):
        x1, y1 = rectangle[0]
        x2, y2 = rectangle[1]
        return x > x1 and x < x2 and y > y1 and y < y2

    def line_crosses_rectangle(self, xa, ya, xb, yb, rectangle):
        x1, y1 = rectangle[0]
        x2, y2 = rectangle[1]
        if ya == yb:
            return min(xa, xb) < x1 and max(xa, xb) > x2 and ya > y1 and ya < y2
        else:
            return min(ya, yb) < y1 and max(ya, yb) > y2 and xa > x1 and xa < x2

start_time = time.time()
# Solve().solve_a('example.txt')
# Solve().solve_a('input.txt')
print("\n")
# Solve().solve_b('example.txt')
Solve().solve_b('input.txt')
print("--- %s seconds ---" % (time.time() - start_time))