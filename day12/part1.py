#!/usr/bin/env python
from collections import defaultdict

with open('example.txt', 'r') as file:
    plots = [list(line) for line in file.read().split("\n") if line != '']
width = len(plots[0])
height = len(plots)

def find_next_region():
    for x in range(width):
        for y in range(height):
            if '*' not in plots[y][x]:
                return [[x, y]]
    return False

def explore_region(region, position, region_type):
    fencing = 0
    plots[region[position][1]][region[position][0]] = f"{region_type}*"
    for x, y in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
        x_pos = region[position][0] + x
        y_pos = region[position][1] + y
        if not x_pos in range(0, width) or not y_pos in range(0, height):
            fencing += 1
        elif plots[y_pos][x_pos] == f"{region_type}*":
            pass
        elif plots[y_pos][x_pos] == region_type:
            if [x_pos, y_pos] not in region:
                region.append([x_pos, y_pos])
        else:
            fencing += 1
    return fencing

print(plots)

next_region = find_next_region()
fencing_cost = 0

while next_region:
    fencing = 0
    region = next_region
    region_type = plots[region[0][1]][region[0][0]]
    position = 0
    while position < len(region):
        fencing += explore_region(region, position, region_type)
        position += 1
    fencing_cost += fencing * len(region)
    next_region = find_next_region()

print(fencing_cost)