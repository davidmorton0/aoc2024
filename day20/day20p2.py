#!/usr/bin/env python
from collections import defaultdict

INPUT = 1
FILENAME = ['example_1.txt', 'input_h.txt', 'input_w.txt'][INPUT]

with open(FILENAME, 'r') as file:
    track = [list(line) for line in file.read().split("\n") if line != ""]

def find_start_end():
    for y, row in enumerate(track):
        for x, pos in enumerate(list(row)):
            if pos == 'S':
                start = [x, y]
            if pos == 'E':
                end = [x, y]
    return [start, end]

start, end = find_start_end()
HEIGHT = len(track)
WIDTH = len(track[0])
print(f"Width={WIDTH}. Height={HEIGHT}")
print(f"Start={start}:{track[start[1]][start[0]]}")
print(f"End={end}:{track[end[1]][end[0]]}")


def show_symbol(position):
    if position in ['.', '#', 'S', 'E']:
        return position
    else:
        return '*'

def print_track():
    for row in track:
        print("".join([show_symbol(c) for c in row]))

def update_neighbours(x, y, n):
    coords = [[x + 1, y], [x - 1, y], [x, y + 1], [x, y - 1]]
    for x1, y1 in coords:
        if x1 in range(0, WIDTH) and y1 in range(0, HEIGHT) and track[y1][x1] in [".", "E"]:
            track[y1][x1] = n

def do_iteration(n):
    for y, row in enumerate(track):
        for x, pos in enumerate(row):
            if pos == n:
                update_neighbours(x, y, n + 1)

def find_exits(x, y):
    MAX_DIST = 20
    exits = []
    for n in range(0, MAX_DIST + 1):
        for m in range(0, MAX_DIST + 1 - n):
            if n + m >= 2:
                poss_exits = [
                    [x + n, y + m, n + m],
                    [x + n, y - m, n + m],
                    [x - n, y + m, n + m],
                    [x - n, y - m, n + m]
                ]
                for exit in poss_exits:
                    if exit not in exits:
                        exits.append(exit)
    return exits


def check_for_shortcuts(x1, y1):
    shortcuts = []
    possible_exits = find_exits(x1, y1)
    for x2, y2, t in possible_exits:
        if x2 in range(WIDTH) and y2 in range(HEIGHT) and track[y2][x2] != '#':
            diff = track[y2][x2] - track[y1][x1]
            if diff > t:
                shortcuts.append([x2, y2, diff - t])
    return shortcuts

def find_shortcuts():
    shortcuts = []
    for y, row in enumerate(track):
        for x, pos in enumerate(list(row)):
            if pos != '#':
                shortcuts.extend(check_for_shortcuts(x, y))
    return shortcuts

n = 0
track[start[1]][start[0]] = n
while track[end[1]][end[0]] == 'E':
    do_iteration(n)
    n += 1


shortcuts = find_shortcuts()
shortcuts_count = defaultdict(lambda: 0)
shortcuts_100 = 0
for x, y, diff in shortcuts:
    shortcuts_count[diff] += 1
    if diff >= 100:
        shortcuts_100 += 1

print(shortcuts_count)
print(shortcuts_100)