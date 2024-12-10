#!/usr/bin/env python

with open('input.txt', 'r') as file:
    grid = []
    for line in file.read().split("\n"):
        grid.append([int(pos) for pos in list(line)])

width = len(grid[0])
height = len([line for line in grid if line != ''])

def find_trailheads(grid):
    trailheads = []
    for y, line in enumerate(grid):
        [trailheads.append([x, y, x, y, 0]) for x, location in enumerate(list(line)) if location == 0]
    return trailheads

def is_valid_path(x, y, m):
    return x in range(0, width) and y in range(0, width) and grid[y][x] == m

def add_next_locations(start_x, start_y, x, y, marker, new_locations):
    for x1, y1 in [[1, 0], [-1, 0], [0, -1], [0, 1]]:
        if is_valid_path(x + x1, y + y1, marker + 1):
            new_locations.append([start_x, start_y, x + x1, y + y1, marker + 1])

def find_next_path(locations):
    new_locations = []
    for location in locations:
        add_next_locations(*location, new_locations)
    return new_locations

locations = find_trailheads(grid)

for _ in range(0, 9):
    locations = find_next_path(locations)

position_strings = [','.join(map(str, location)) for location in locations]
unique_locations = set(position_strings)
print(len(unique_locations))
print(len(locations))
