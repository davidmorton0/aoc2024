#!/usr/bin/env python

from path import Path

FILENAME = 'input_h.txt'

with open(FILENAME, 'r') as file:
    maze = [list(line) for line in file.read().split("\n") if line != ""]

START = [1, len(maze) - 2]
END = [len(maze[0]) - 2, 1]
c_x, c_y = START
MAX_SCORE = [7036, 11048, 73432][2]

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

def check_success(path):
    if path.latest_location() == END:
        path.status = 'success'
    if path.current_score() > MAX_SCORE:
        path.status = 'ended'

def extend_path(path):
    valid_exits = [exit for exit in find_exits(*path.latest_location()) if exit not in path.locations]
    if valid_exits:
        if len(valid_exits) > 1:
            for exit in valid_exits[1:]:
                if exit not in path.locations:
                    new_path = duplicate_path(path)
                    new_path.add_to_path(exit)
                    paths.append(new_path)
        if valid_exits[0] not in path.locations:
            path.add_to_path(valid_exits[0])
        else:
            path.status = 'ended'
    else:
        path.status = 'ended'

initial_path = Path(locations=[START])
paths = [initial_path]

checking_paths = [path for path in paths if path.status in 'in_progress']

while checking_paths:
# for _ in range(0, 50):
    for path in checking_paths:
        extend_path(path)
        check_success(path)
    print(len(paths))
    print(len(checking_paths))
    print(checking_paths[-1].current_score())
    print()
    checking_paths = [path for path in paths if path.status == 'in_progress']

locations = []
for path in [path for path in paths if path.status == 'success']:
    locations.extend([location for location in path.locations if location not in locations])
    print(len(locations))
