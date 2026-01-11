#!/usr/bin/env python
from math import inf

INPUT = 2
FILENAME = ['example_1.txt', 'example_2.txt', 'input_w.txt', 'input_w.txt'][INPUT]
DIRECTIONS = ['<','>','^','v']

def create_location(symbol):
    return {
        "active": False,
        "checked": False,
        "removed": False,
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

def select_best_path_symbol(location):
    if not location["removed"] and location["checked"]:
        return '*'
    else:
        return location["symbol"]


def print_maze_best_paths():
    for row in maze:
        print("".join([select_best_path_symbol(location) for location in row]))

def print_result():
    for row in maze:
        result = [location for location in row if location["symbol"] == 'E']
        if result:
            print(result)

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
LOWEST_SCORE = 7036
start_x, start_y = START
end_x, end_y = END

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
        "removed": False,
        "symbol": "S",
        "scores": {
            "<": 1000,
            "^": 1000,
            "v": 1000,
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
    in_progress = iteration()


def check_location(x, y, direction1):
    results = []
    score1 = maze[y][x]["scores"][direction1]
    for direction2, score2 in maze[y][x]["scores"].items():
        if score2 == score1 - 1000:
           results.append([x, y, direction2])
    return results

def check_neighbour(x1, y1, direction):
    score = maze[y1][x1]["scores"][direction]
    if direction == '^':
        x2, y2 = [x1, y1 + 1]
    elif direction == 'v':
        x2, y2 = [x1, y1 - 1]
    elif direction == '<':
        x2, y2 = [x1 + 1, y1]
    elif direction == '>':
        x2, y2 = [x1 - 1, y1]
    if maze[y2][x2]["scores"][direction] + 1 == score:
        return [[x2, y2, direction]]
    else:
        return []

def path_at_start(path):
    return path[-1] == [start_x, start_y, ">"]

def paths_to_check(paths):
    return [path for path in paths if not path_at_start(path)]

paths = [[[end_x, end_y, '^']]]

while paths_to_check(paths):
    new_paths = []
    for path in paths:
        results = check_location(*path[-1])
        results.extend(check_neighbour(*path[-1]))
        for result in results:
            new_paths.append([*path, result])
    paths = new_paths

all_locations = []
for path in paths:
    for x, y, d in path:
        if [x, y] not in all_locations:
            all_locations.append([x, y])
print(len(all_locations))

print_result()

