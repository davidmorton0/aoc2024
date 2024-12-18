#!/usr/bin/env python

FILENAME = 'input_w.txt'
best_score = 776584

with open(FILENAME, 'r') as file:
    maze = [list(line) for line in file.read().split("\n") if line != ""]

START = [1, len(maze) - 2]
c_x, c_y = START

print(f"Width={len(maze[0])}. Height={len(maze)}")
print(f"Start={START}:{maze[c_y][c_x]}")

def find_exits(x1, y1):
    exits = []
    possible_exits = [[x1 + 1, y1], [x1 - 1, y1], [x1, y1 + 1], [x1, y1 - 1]]
    for x2, y2 in possible_exits:
        if maze[y2][x2] in ['.', 'E']:
            exits.append([x2, y2])
    return exits

paths = [[[*START]]]

