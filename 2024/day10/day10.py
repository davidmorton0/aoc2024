#!/usr/bin/env python
import time
from itertools import product

start_time = time.time()

def load_input(filename):
    with open(filename, 'r') as file:
        lines = [line for line in file.read().split("\n") if line != ""]
        grid = []
        for line in lines:
            grid.append([int(pos) for pos in list(line)])
        return grid

def find_markers(grid, width, height, marker):
    return [[x, y] for x, y in product(range(width), range(height)) if grid[y][x] == marker]

def add_next_locations(location, new_locations, grid):
    start_x, start_y, x, y, marker = location
    height = len(grid)
    width = len(grid[0])
    for x1, y1 in [[1, 0], [-1, 0], [0, -1], [0, 1]]:
        if x + x1 in range(width) and y + y1 in range(height) and grid[y + y1][x + x1] == marker + 1:
            new_locations.append([start_x, start_y, x + x1, y + y1, marker + 1])

def find_next_location(locations, grid):
    new_locations = []
    for location in locations:
        add_next_locations(location, new_locations, grid)
    return new_locations

def next_locations(x, y, marker, grid):
    height = len(grid)
    width = len(grid[0])
    markers = find_markers(grid, width, height, marker + 1)
    return [[x1, y1] for x1, y1 in markers if abs(x - x1) + abs(y - y1) == 1]

def find_next_path(path, grid):
    x, y, marker = path[-1]
    new_paths = []
    for x1, y1 in next_locations(x, y, marker, grid):
        new_paths.append([*path.copy(), [x1, y1, marker + 1]])
    return new_paths

def solve(filename):
    grid = load_input(filename)
    height = len(grid)
    width = len(grid[0])

    trailheads = find_markers(grid, width, height, 0)
    path_locations = [[x, y, x, y, 0] for x, y in trailheads]
    for _ in range(0, 9):
        path_locations = find_next_location(path_locations, grid)
    position_strings = [','.join(map(str, location)) for location in path_locations]
    unique_locations = set(position_strings)
    print(f"Filename: {filename}")
    print(f"Part 1: {len(unique_locations)}")
    print(f"Part 2: {len(path_locations)}\n")

solve('example.txt')
solve('input_w.txt')
solve('input_h.txt')

print("--- %s seconds ---" % (time.time() - start_time))