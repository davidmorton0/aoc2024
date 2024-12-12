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

def in_plots(x, y):
    return x in range(0, width) and y in range(0, height)

def explore_region(region, position, region_type):
    fencing = 0
    plots[region[position][1]][region[position][0]] = f"{region_type}*"
    for x, y in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
        x_pos = region[position][0] + x
        y_pos = region[position][1] + y
        if not in_plots(x_pos, y_pos):
            fencing += 1
        elif plots[y_pos][x_pos] == f"{region_type}*":
            pass
        elif plots[y_pos][x_pos] == region_type:
            if [x_pos, y_pos] not in region:
                region.append([x_pos, y_pos])
        else:
            fencing += 1
    return fencing

def check_corners_direction(check_plots, region, region_type):
    corners = 0
    can_check = True
    print(check_plots)
    for check_plot in check_plots:
        can_check = can_check and in_plots(*check_plot)

    if not can_check:
        print("Skip")
    # print([region_type, plots[y + 1][x + 1], plots[y + 1][x], plots[y][x + 1]])
    elif plots[y + 1][x + 1] != region_type and (plots[y + 1][x] == region_type and plots[y][x + 1] == region_type) or (
            plots[y + 1][x] != region_type and plots[y][x + 1] != region_type):
        print(True)
        corners += 1
    else:
        print(False)
    return corners


def count_corners(region, region_type):
    corners = 0
    for x, y in region:
        # bottom right corner
        check_corners_direction([[x + 1, y + 1], [x, y + 1], [x + 1, y], region, region_type])
    print(region_type)
    print(corners)

print(plots)

next_region = find_next_region()
fencing_cost = 0

# while next_region:
fencing = 0
region = next_region
region_type = plots[region[0][1]][region[0][0]]
plots[region[0][1]][region[0][0]] = f"{region_type}*"
position = 0
while position < len(region):
    fencing += explore_region(region, position, region_type)
    position += 1
fencing_cost += fencing * len(region)
print(plots)

count_corners(region, f"{region_type}*")
next_region = find_next_region()

print(fencing_cost)