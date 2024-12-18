#!/usr/bin/env python
from math import inf

INPUT = 0
FILENAME = ['example_1.txt', 'example_2.txt', 'input_h.txt', 'input_w.txt'][INPUT]
DIRECTIONS = ['<','>','^','v']

def create_location(symbol):
    return {
        "active": False,
        "checked": False,
        "symbol": symbol,
        "scores": {
            "<": inf,
            "^": inf,
            "v": inf,
            ">": inf
        }
    }

def select_symbol(location):
    if location["checked"]:
        return '*'
    else:
        return location["symbol"]

def print_maze():
    for row in maze:
        print("".join([select_symbol(location) for location in row]))

def print_locations():
    for y, row in enumerate(maze):
        print([[[x, y], location] for x, location in enumerate(row) if location["checked"]])

maze = []
with open(FILENAME, 'r') as file:
    for line in file.read().split("\n"):
        if line == "":
            continue
        maze.append([create_location(symbol) for symbol in list(line)])

START = [1, len(maze) - 2]
END = [len(maze[0]) - 2, 1]
start_x, start_y = START

def find_exits(x1, y1):
    exits = []
    possible_exits = [[x1 + 1, y1], [x1 - 1, y1], [x1, y1 + 1], [x1, y1 - 1]]
    for x2, y2 in possible_exits:
        if maze[y2][x2]["symbol"] in ['.', 'E']:
            exits.append([x2, y2])
    return exits

def activate_location(location, exit_location, main_direction):
    if exit_location["symbol"] in [".", "E"]:
        exit_location["checked"] = True
        exit_score1 = location["scores"][main_direction] + 1
        exit_score2 = location["scores"][main_direction] + 1001
        if exit_location["scores"][main_direction] > exit_score1:
            exit_location["scores"][main_direction] = exit_score1
            exit_location["active"] = True
        other_directions = [direction for direction in DIRECTIONS if direction != main_direction]
        for direction in other_directions:
            if exit_location["scores"][direction] > exit_score2:
                exit_location["scores"][direction] = exit_score2
                exit_location["active"] = True

maze[start_y][start_x] = {
        "active": True,
        "checked": True,
        "symbol": "S",
        "scores": {
            "<": 0,
            "^": 0,
            "v": 0,
            ">": 0
        }
    }

def iteration():
    has_checked = False
    for y, row in enumerate(maze):
        for x, location in enumerate(row):
            if location["active"]:
                has_checked = True
                north_exit = maze[y - 1][x]
                activate_location(location, north_exit, "^")
                east_exit = maze[y][x - 1]
                activate_location(location, east_exit, "<")
                west_exit = maze[y][x + 1]
                activate_location(location, west_exit, ">")
                south_exit = maze[y + 1][x]
                activate_location(location, south_exit, "v")
                location["active"] = False
    return has_checked

in_progress = True
while in_progress:
    print_maze()
    print()
    in_progress = iteration()

# for _ in range(0, 5):
#     print_maze()
#     print_locations()
#     iteration()

print_locations()

