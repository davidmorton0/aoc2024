#!/usr/bin/env python
from itertools import combinations

with open('input.txt', 'r') as file:
    input = file.read().split("\n")

width = len(input[0])
height = len([line for line in input if line != ''])
grid = []

for line in input:
    grid.append([int(pos) for pos in list(line)])

def find_trailsheads(grid):
    trailheads = []
    for y, line in enumerate(grid):
        for x, position in enumerate(list(line)):
            if position == 0:
                trailheads.append([x, y, x, y, 0])
    return trailheads

def in_range_x(x):
    return x in range(0, width)

def in_range_y(y):
    return y in range(0, height)

def check_new_position(x, y, m):
    return in_range_x(x) and in_range_y(y) and grid[y][x] == m

# def check_new_positions():

def find_next_path(positions):
    new_positions = []
    for position in positions:
        new_marker = position[4] + 1

        new_position_x = position[2] - 1
        new_position_y = position[3]
        if check_new_position(new_position_x, new_position_y, new_marker):
            new_positions.append([position[0], position[1], new_position_x, new_position_y, new_marker])

        new_position_x = position[2] + 1
        new_position_y = position[3]
        if check_new_position(new_position_x, new_position_y, new_marker):
            new_positions.append([position[0], position[1], new_position_x, new_position_y, new_marker])

        new_position_x = position[2]
        new_position_y = position[3] - 1
        if check_new_position(new_position_x, new_position_y, new_marker):
            new_positions.append([position[0], position[1], new_position_x, new_position_y, new_marker])

        new_position_x = position[2]
        new_position_y = position[3] + 1
        if check_new_position(new_position_x, new_position_y, new_marker):
            new_positions.append([position[0], position[1], new_position_x, new_position_y, new_marker])
    return new_positions

positions = find_trailsheads(grid)

while positions[0][4] < 9:
    positions = find_next_path(positions)

position_strings = []
for position in positions:
    position_strings.append(','.join([str(n) for n in position]))
unique_positions = set(position_strings)
print(len(positions))
print(len(unique_positions))
