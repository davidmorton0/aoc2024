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
        self.create_grid(coordinates)
        self.paint_outline(coordinates)
        print("\n")
        self.print_grid()

    def create_grid(self, coordinates):
        x_coordinates = [c[0] for c in coordinates]
        x_coordinates.sort()
        y_coordinates = [c[1] for c in coordinates]
        y_coordinates.sort()
        print(x_coordinates)
        print(y_coordinates)
        line = []
        line.append(
            self.rectangle(
                0, 0, x_coordinates[0], y_coordinates[0], 0, 0
            )
        )
        for x in x_coordinates:
            line.append(
            self.rectangle(
                line[-1]["x_end"], line[-1]["y_end"], x, 0, line[-1]["x_index"] + 1, 0
            )
        )
        print(line)



        # max_x, max_y = coordinates[0]
        # min_x, min_y = coordinates[0]
        # for x, y in coordinates:
        #     if x > max_x:
        #         max_x = x
        #     elif x < min_x:
        #         min_x = x
        #     if y > max_y:
        #         max_y = y
        #     elif y < min_y:
        #         min_y = y
        # self.offset_x = min_x - 1
        # self.offset_y = min_y - 1
        # self.range_x = max_x - self.offset_x + 1
        # self.range_y = max_y - self.offset_y + 1
        # print(self.offset_x, self.range_x)
        # print(self.offset_y, self.range_y)
        # for y in range(self.offset_y, self.offset_y + self.range_y + 1):
        #     self.grid.append(list("." * (self.range_x + 1)))

    def rectangle(self, x1, y1, x2, y2, xi, yi):
        return {
            "x_start": min(x1, x2),
            "x_end": max(x1, x2),
            "y_start": min(y1, y2),
            "y_end": max(y1, y2),
            "x_index": xi,
            "y_index": yi,
            "size": abs(x1 - x2) * abs(y1 - y2)
        }

    def print_grid(self):
        pass
        # for line in self.grid:
        #     print("".join(line))

    def paint_outline(self, coordinates):
        pass
        # for n, [c_x, c_y] in enumerate(coordinates):
        #     p_x, p_y = coordinates[n-1]
        #     print([c_x, c_y], [p_x, p_y])
        #     if p_x == c_x:
        #         print(list(range(min([c_y, p_y]), max(c_y, p_y + 1))))
        #         for y in range(min([c_y, p_y]), max(c_y, p_y) + 1):
        #             self.set_value(c_x, y, "R")
        #     else:
        #         print(list(range(min([c_x, p_x]), max(c_x, p_x) + 1)))
        #         for x in range(min([c_x, p_x]), max(c_x, p_x) + 1):
        #             self.set_value(x, c_y, "R")

    # def set_value(self, x, y, colour):
    #     self.grid[y - self.offset_y][x - self.offset_x] = colour







start_time = time.time()
# Solve().solve_a('example.txt')
# Solve().solve_a('input.txt')
print("\n")
Solve().solve_b('example.txt')
# Solve().solve_b('input.txt')
print("--- %s seconds ---" % (time.time() - start_time))