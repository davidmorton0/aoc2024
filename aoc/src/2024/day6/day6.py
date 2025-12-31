#!/usr/bin/env python

from copy import deepcopy

with open('input.txt', 'r') as file:
    input = file.read().split()
grid = [list(line) for line in input]

height = len(input)
width = len(input[0])

GUARD_ICONS = ['^', '<', 'v', '>']

def find_grid_positions():
    obstacles = []
    for y, row in enumerate(grid):
        for x, pos in enumerate(list(row)):
            if pos == '#':
                obstacles.append([x, y])
            elif pos in GUARD_ICONS:
                guard_position = [pos, x, y]
    return [guard_position, obstacles]

def turn_guard_right(facing):
    return GUARD_ICONS[GUARD_ICONS.index(facing) - 1]

def move_guard(guard_position, obstacles):
    facing, guard_x, guard_y = guard_position
    match facing:
        case '^': x, y = guard_x, guard_y - 1
        case '>': x, y = guard_x + 1, guard_y
        case 'v': x, y = guard_x, guard_y + 1
        case '<': x, y = guard_x - 1, guard_y

    if x not in range(width) or y not in range(height):
        return ['*', -1, -1]
    elif [x, y] in obstacles:
        return [turn_guard_right(facing), guard_x, guard_y]
    else:
        return [facing, x, y]

def find_guard_path(guard_position, obstacles):
    path = [guard_position]
    while True:
        guard_position = move_guard(guard_position, obstacles)
        if guard_position[0] == '*':
            return [False, path]
        elif guard_position in path:
            return [True, path]
        else:
            path.append(guard_position)

guard_position, obstacles = find_grid_positions()
_, initial_path = find_guard_path(guard_position, obstacles)
print(f"Initial path length: {len(initial_path)}")

new_obstacle_locations = []
for _, x, y in initial_path:
    if [x, y] not in new_obstacle_locations:
        new_obstacle_locations.append([x, y])

new_obstacles_count = len(new_obstacle_locations)
print(f"New obstacles: {new_obstacles_count}")

count = 0
for o, new_obstacle_location in enumerate(new_obstacle_locations):
    print(f"Checking obstacle: {o}/{new_obstacles_count}")
    guard_position, obstacles = find_grid_positions()
    obstacles.append(new_obstacle_location)
    result, path = find_guard_path(guard_position, obstacles)
    if result:
        count += 1

print(count)


