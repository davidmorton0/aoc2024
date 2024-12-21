#!/usr/bin/env python
from collections import defaultdict

INPUT = 1
FILENAME = ['example.txt', 'input_h.txt', 'input_w.txt'][INPUT]
MIN_CHEAT_SIZE_1 = [2, 100, 100][INPUT]
MIN_CHEAT_SIZE_2 = [50, 100, 100][INPUT]

with open(FILENAME, 'r') as file:
    track = [list(line) for line in file.read().split("\n") if line != ""]

def find_locations():
    path_locations = []
    for y, row in enumerate(track):
        for x, pos in enumerate(list(row)):
            match pos:
                case 'S': start = [x, y]
                case 'E': end = [x, y]
                case '.': path_locations.append([x, y])
    return [start, end, path_locations]


def show_symbol(position):
    if position in ['.', '#', 'S', 'E']:
        return position
    else:
        return '*'

def print_track():
    for row in track:
        print("".join([show_symbol(c) for c in row]))

def count_shortcuts(n, path):
    shortcuts = []
    x1, y1 = path[n]
    remaining_path = path[n:]
    for m, [x2, y2] in enumerate(remaining_path):
        distance_moved = abs(x2 - x1) + abs(y2 - y1)
        if distance_moved == 2 and m > 2:
            shortcuts.append([x2, y2, m - 2])
    return shortcuts

def count_shortcuts2(n, path):
    shortcuts = []
    x1, y1 = path[n]
    remaining_path = path[n:]
    for m, [x2, y2] in enumerate(remaining_path):
        distance_moved = abs(x2 - x1) + abs(y2 - y1)
        if distance_moved >= 2 and m > distance_moved:
            shortcuts.append([x2, y2, m - distance_moved])
    return shortcuts

def find_neighbours(x, y, path_locations):
    for loc in [[x + 1, y], [x - 1, y], [x, y + 1], [x, y - 1]]:
        if loc in path_locations:
            return loc

start, end, path_locations = find_locations()
HEIGHT = len(track)
WIDTH = len(track[0])
print(f"Width={WIDTH}. Height={HEIGHT}")
print(f"Start={start}:{track[start[1]][start[0]]}")
print(f"End={end}:{track[end[1]][end[0]]}")

path = [start]
while path_locations:
    loc = find_neighbours(*path[-1], path_locations)
    path.append(path_locations.pop(path_locations.index(loc)))
path.append(end)

print_track()

shortcuts = []
shortcuts2 = []
for n in range(len(path)):
    shortcuts.extend(count_shortcuts(n, path))
    shortcuts2.extend(count_shortcuts2(n, path))

shortcuts_count = defaultdict(lambda: 0)
for x, y, n in shortcuts:
    if n >= MIN_CHEAT_SIZE_1:
        shortcuts_count[n] += 1

sc = list(shortcuts_count.items())
sc.sort()
print(sc)
print(sum(shortcuts_count.values()))

shortcuts_count2 = defaultdict(lambda: 0)
for x, y, n in shortcuts2:
    if n >= MIN_CHEAT_SIZE_2:
        shortcuts_count2[n] += 1

sc2 = list(shortcuts_count2.items())
sc2.sort()
print(sc2)
print(sum(shortcuts_count2.values()))
