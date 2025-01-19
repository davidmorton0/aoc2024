#!/usr/bin/env python
from path import Path

FILENAME = 'input_w.txt'

with open(FILENAME, 'r') as file:
    maze = [list(line) for line in file.read().split("\n") if line != ""]

START = [1, len(maze) - 2]
END = [len(maze[0]) - 2, 1]
c_x, c_y = START

print(f"Width={len(maze[0])}. Height={len(maze)}")
print(f"Start={START}:{maze[c_y][c_x]}")

def print_paths():
    print("Printing paths")
    for path in paths:
        print(f"status:{path.status}. locations: {path.locations}. score: {path.current_score()}")
    print()

def duplicate_path(path):
    return Path(locations=path.locations.copy())

def find_exits(x1, y1):
    exits = []
    possible_exits = [[x1 + 1, y1], [x1 - 1, y1], [x1, y1 + 1], [x1, y1 - 1]]
    for x2, y2 in possible_exits:
        if maze[y2][x2] in ['.', 'E']:
            exits.append([x2, y2])
    return exits

def check_collision(path):
    for check_path in paths:
        if path == check_path or check_path.status == 'ended':
            continue
        if path.locations[-1] in check_path.locations:
            path_score = path.current_score()
            path_up_to = check_path.path_up_to(check_path.find_in_path(path.locations[-1]) + 1)
            check_path_score = check_path.calculate_score(path_up_to)
            # print(f"Path:{path.locations} Path score: {path_score}")
            # print(f"Path:{check_path.locations}. Path up to:{path_up_to} Path score: {check_path_score}")
            if check_path_score >= path_score:
                check_path.status = 'ended'
            else:
                path.status = 'ended'

def check_success(path):
    if path.latest_location() == END:
        path.status = 'success'

def extend_path(path):
    valid_exits = [exit for exit in find_exits(*path.latest_location()) if exit not in path.locations]
    # print("exits")
    # print(valid_exits)
    # print()
    if valid_exits:
        if len(valid_exits) > 1:
            for exit in valid_exits[1:]:
                new_path = duplicate_path(path)
                new_path.add_to_path(exit)
                paths.append(new_path)
        path.add_to_path(valid_exits[0])
    else:
        path.status = 'ended'

initial_path = Path(locations=[START])
paths = [initial_path]

print_paths()
checking_paths = [path for path in paths if path.status == 'in_progress']

while checking_paths:
# for _ in range(0, 50):
    for path in checking_paths:
        extend_path(path)
    for path in checking_paths:
        check_collision(path)
        check_success(path)
    # print_paths()
    checking_paths = [path for path in paths if path.status == 'in_progress']

for path in [path for path in paths if path.status == 'success']:
    print(path.locations)
    print(path.current_score())
