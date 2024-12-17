#!/usr/bin/env python
from path import Path

FILENAME = 'example_1.txt'

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
        print(f"status:{path.status}. locations: {path.locations}")
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

def handle_collision(checking_path):
    for path in checking_paths:
        if path == checking_path:
            continue
        if checking_path.is_collision(path):
            print(path.locations)
            print(checking_path.locations)
            print()
            checking_path_score = checking_path.current_score()
            path_up_to = path.path_up_to(path.find_in_path(checking_path.latest_location()))
            path_score = path.calculate_score(path_up_to)
            if checking_path_score >= path_score:
                checking_path.status = 'ended'
            else:
                path.status = 'ended'

def check_success(path):
    if path.latest_location() == END:
        path.status = 'success'

def extend_path(path):
    valid_exits = [exit for exit in find_exits(*path.latest_location()) if exit not in path.locations]
    print("exits")
    print(valid_exits)
    print()
    if valid_exits:
        if len(valid_exits) > 1:
            for exit in valid_exits[1:]:
                new_path = duplicate_path(path)
                new_path.add_to_path(exit)
                paths.append(new_path)
                handle_collision(new_path)
        path.add_to_path(valid_exits[0])
        handle_collision(path)
    else:
        path.status = 'ended'

initial_path = Path(locations=[START])
paths = [initial_path]

print_paths()
checking_paths = [path for path in paths if path.status == 'in_progress']

while checking_paths:
    for path in checking_paths:
        extend_path(path)
    print_paths()
    checking_paths = [path for path in paths if path.status == 'in_progress']

for path in [path for path in paths if path.status == 'success']:
    print(path.locations)
    print(path.current_score())


# failed_paths = []
# success_paths = []
# for _ in range(0, 5):
#     new_paths = []
#     for path in paths:
#         add_paths = extend_path(path)
#         if add_paths:
#             for add_path in add_paths:
#                 if add_path[-1] == END:
#                     success_paths.append(add_path)
#                 else:
#                     collision = False
#
#
#                     new_paths.append(add_path)
#         else:
#             failed_paths.append(path)
#     paths = new_paths
#     print(paths)
#     print(failed_paths)

