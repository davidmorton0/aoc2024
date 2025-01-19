#!/usr/bin/env python
from time import time

start_time = time()

def load_input(filename):
    with open(filename, 'r') as file:
        plots = [list(line) for line in file.read().split("\n") if line != '']
    return plots

def find_next_region(plots, width, height):
    for x in range(width):
        for y in range(height):
            if '*' not in plots[y][x]:
                return [[x, y]]
    return False

def in_plots(x, y, width, height):
    return x in range(width) and y in range(height)

def explore_region(region, position, region_type, plots, width, height):
    fencing = 0
    plots[region[position][1]][region[position][0]] = f"{region_type}*"
    for x, y in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
        x_pos = region[position][0] + x
        y_pos = region[position][1] + y
        if not in_plots(x_pos, y_pos, width, height):
            fencing += 1
        elif plots[y_pos][x_pos] == f"{region_type}*":
            pass
        elif plots[y_pos][x_pos] == region_type:
            if [x_pos, y_pos] not in region:
                region.append([x_pos, y_pos])
        else:
            fencing += 1
    return fencing

def check_corner(corner, region):
    if corner[0] not in region and corner[1] in region and corner[2] in region:
        return True
    elif corner[1] not in region and corner[2] not in region:
        return True
    return False

def count_corners(region):
    corner_count = 0
    for x, y in region:
        corners = [
            [[x + 1, y + 1], [x, y + 1], [x + 1, y]],
            [[x + 1, y - 1], [x + 1, y], [x, y - 1]],
            [[x - 1, y - 1], [x - 1, y], [x, y - 1]],
            [[x - 1, y + 1], [x - 1, y], [x, y + 1]],
        ]
        for corner in corners:
            if check_corner(corner, region):
                corner_count += 1
    return corner_count

def solve(filename):
    print(f"Filename: {filename}")

    plots = load_input(filename)
    width = len(plots[0])
    height = len(plots)

    fencing_cost = 0
    bulk_fencing_cost = 0

    while region := find_next_region(plots, width, height):
        region_type = plots[region[0][1]][region[0][0]]
        plots[region[0][1]][region[0][0]] = f"{region_type}*"

        fencing = 0
        position = 0
        while position < len(region):
            fencing += explore_region(region, position, region_type, plots, width, height)
            position += 1
        fencing_cost += fencing * len(region)
        bulk_fencing_cost += count_corners(region) * len(region)

    print(f"Part 1 fencing cost: {fencing_cost}")
    print(f"Part 2 bulk fencing cost: {bulk_fencing_cost}\n")

solve('example.txt')
solve('input.txt')

print("--- %s seconds ---" % (time() - start_time))