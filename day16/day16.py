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

def find_next_path(path):
    while len(path) > 1:
        previous_location = path.pop()
        current_location = path[-1]
        x, y = current_location
        valid_exits = [exit for exit in find_exits(x, y) if exit not in path]
        if valid_exits and valid_exits[-1] != previous_location:
            new_path = path + [valid_exits[valid_exits.index(previous_location) + 1]]
            return extend_path(new_path)
    return False, False

def extend_path(path):
    x, y = path[-1]
    while maze[y][x] != 'E':
        exits = find_exits(x, y)
        valid_exits = [exit for exit in exits if exit not in path]
        if len(valid_exits) == 0 or score_path(path) > best_score:
            return path, False
        path.append(valid_exits[0])
        x, y = path[-1]
    return path, True

def score_path(path):
    previous_moving_direction=None
    score = 0
    for n, [x, y] in enumerate(path[1:]):
        prev_x, prev_y = path[n - 1]
        if x != prev_x:
            current_moving_direction = 'NS'
        else:
            current_moving_direction = 'EW'

        if previous_moving_direction and current_moving_direction != previous_moving_direction:
            score += 1001
        else:
            score += 1
        previous_moving_direction = current_moving_direction
    return score

def find_next_valid_path(path):
    next_path, success = find_next_path(path)
    while next_path:
        if success:
            return next_path
        next_path, success = find_next_path(next_path)
    return False

current_path, success = extend_path([START])
# if success:
#     best_score = score_path(current_path)
#     best_path = current_path
# else:
#     best_score = 100000000000

print(current_path)
print(success)
if success:
    score = score_path(current_path)
    if best_score > score:
        best_score = score

current_path = find_next_valid_path(current_path)
valid_paths = 2

while(current_path):
    score = score_path(current_path)
    print(score)
    if best_score > score:
        best_score = score
    current_path = find_next_valid_path(current_path)
    valid_paths += 1
    print(best_score)
    print(valid_paths)
print()
print(best_score)

# valid_path = True
# while valid_path:
#     valid_path = find_next_valid_path(current_path)
#     print(valid_path)
#     if valid_path:
#         valid_path_score = score_path(valid_path)
#         if best_score > valid_path_score:
#             best_score = valid_path_score
#             best_path = valid_path
#             print(best_path)
#             print(best_score)
#
# print(best_path)
# print(best_score)


# while p1:
#     while not success:
#         p2, success = next_path(p1)
#         if not p2:
#             break
#     if not p2:
#         break
#     score = score_path(p2)
#     print(p2)
#     print(score)
#     if score < best_score:
#         best_score = score
#         best_path = p2
#     success = False
# print(best_path)
# print(best_score)

# print([score_path(path) for path in complete_paths])
# print(min([score_path(path) for path in complete_paths]))