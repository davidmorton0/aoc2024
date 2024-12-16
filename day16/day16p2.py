#!/usr/bin/env python
import re
import time

example = False
if example:
    width = 11
    height = 7
    filename = 'example_1.txt'
else:
    width = 101
    height = 103
    filename = 'input.txt'

midpoint_x = int((width - 1) / 2)
midpoint_y = int((height - 1) / 2)

REGEX = r'p=(-?\d+),(-?\d+) v=(-?\d+),(-?\d+)'

with open(filename, 'r') as file:
    input = [line for line in file.read().split("\n") if line != ""]

robots = []
for line in input:
    match = re.match(REGEX, line)
    robots.append({"p": [int(match[1]), int(match[2])], "v": [int(match[3]), int(match[4])]})

def find_quadrant(x, y):
    quadrant = 0
    if x == midpoint_x or y == midpoint_y:
        return 4
    if x > midpoint_x:
        quadrant += 1
    if y > midpoint_y:
        quadrant += 2
    return quadrant

quadrant_count = [0,0,0,0,0]
# 114

frames = width * height
start_n = 13
s = 27
t = 103
for n in range(start_n, start_n + frames, 101):
    line = [' '] * width
    grid = []
    for _ in range(0, height):
        grid.append(line.copy())
    for robot in robots:
        x = (robot["p"][0] + robot["v"][0] * n) % width
        y = (robot["p"][1] + robot["v"][1] * n) % height
        grid[y][x] = '*'
    print(n)
    [print(''.join(line)) for line in grid]
    print()
    time.sleep(0.1)
