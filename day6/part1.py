#!/usr/bin/env python

from copy import deepcopy

with open('example.txt', 'r') as file:
    input = file.read().split()
grid = [list(line) for line in input]

height = len(input)
width = len(input[0])

GUARD_ICONS = ['^', '>', '<', 'v']

def calculate_guard_position(grid):
    for y, line in enumerate(grid):
        icon = ''.join(set(line) & set(GUARD_ICONS))
        if icon:
            return [icon, y, line.index(icon)]
    return ['*', 0, 0]

def move_guard(icon, guard_x, guard_y, grid):
    match icon:
        case '^':  # face up
            grid[guard_y][guard_x] = 'X'
            grid[guard_y - 1][guard_x] = icon
        case '>':  # face right
            grid[guard_y][guard_x] = 'X'
            grid[guard_y][guard_x + 1] = icon
        case 'v':  # face down
            grid[guard_y][guard_x] = 'X'
            grid[guard_y + 1][guard_x] = icon
        case '<':  # face down
            grid[guard_y][guard_x] = 'X'
            grid[guard_y][guard_x - 1] = icon
    return grid

def turn_guard(icon, guard_x, guard_y, grid):
    match icon:
        case '^':
            grid[guard_y][guard_x] = '>'
        case '>':
            grid[guard_y][guard_x] = 'v'
        case 'v':
            grid[guard_y][guard_x] = '<'
        case '<':
            grid[guard_y][guard_x] = '^'
    return grid

def do_guard_turn(icon, guard_x, guard_y, grid):
    match icon:
      case '^': #face up
        new_x = guard_x
        new_y = guard_y - 1
      case '>':  # face right
        new_x = guard_x + 1
        new_y = guard_y
      case 'v': #face down
        new_x = guard_x
        new_y = guard_y + 1
      case '<':  # face left
        new_x = guard_x - 1
        new_y = guard_y

    if new_x < width and new_x >= 0 and new_y < height and new_y >= 0:
        if grid[new_y][new_x] in ['.', 'X']:
          move_guard(icon, guard_x, guard_y, grid)
        elif grid[new_y][new_x] == '#':
          turn_guard(icon, guard_x, guard_y, grid)
    else:
        grid[guard_y][guard_x] = 'X'
    return grid

def do_guard_turn_with_checking(icon, guard_x, guard_y, grid):
    match icon:
      case '^': #face up
        new_x = guard_x
        new_y = guard_y - 1
      case '>':  # face right
        new_x = guard_x + 1
        new_y = guard_y
      case 'v': #face down
        new_x = guard_x
        new_y = guard_y + 1
      case '<':  # face left
        new_x = guard_x - 1
        new_y = guard_y

    new_grid = False
    if new_x < width and new_x >= 0 and new_y < height and new_y >= 0:
        if grid[new_y][new_x] in ['.']:
          move_guard(icon, guard_x, guard_y, grid)
          new_grid = True
        elif grid[new_y][new_x] in ['X']:
          move_guard(icon, guard_x, guard_y, grid)
        elif grid[new_y][new_x] == '#':
          turn_guard(icon, guard_x, guard_y, grid)
    else:
        grid[guard_y][guard_x] = 'X'
    return grid, new_grid

def print_grid(grid):
    for line in grid:
        print(''.join(line))

def run_guard(grid):
    icon, guard_y, guard_x = calculate_guard_position(grid)
    while icon != '*':
        grid = do_guard_turn(icon, guard_x, guard_y, grid)
        icon, guard_y, guard_x = calculate_guard_position(grid)
    return grid.copy()

def check_grid_equality(grid1, grid2):
    grid1_joined = ''.join([''.join(line) for line in grid1])
    grid2_joined = ''.join([''.join(line) for line in grid2])
    return grid1_joined == grid2_joined

def run_guard_with_checking(grid):
    icon, guard_y, guard_x = calculate_guard_position(grid)
    old_grids = []
    while icon != '*':
        grid, check = do_guard_turn_with_checking(icon, guard_x, guard_y, grid)
        icon, guard_y, guard_x = calculate_guard_position(grid)
        if not check:
            old_grids.append(deepcopy(grid))
    return grid.copy()

def generate_new_grids(grid_with_xs, initial_grid):
    grids_to_check = []
    for y, line in enumerate(grid_with_xs):
        for x, pos in enumerate(line):
            if pos == 'X':
                new_grid = deepcopy(initial_grid)
                new_grid[y][x] = '#'
                grids_to_check.append(new_grid)
    return grids_to_check

initial_grid = deepcopy(grid)
grid_with_xs = run_guard(grid)
print(sum([len([pos for pos in line if pos == 'X']) for line in grid_with_xs]))

grids_to_check = generate_new_grids(grid_with_xs, initial_grid)

def check_grids():
    for grid_to_check in grids_to_check:



# for n in list(range(0, 200000)):
#     icon, guard_y, guard_x = calculate_guard_position(grid)
#     if icon == '*':
#       print_grid(grid)
#       print('finished')
#       print(sum([len([pos for pos in line if pos == 'X']) for line in grid]))
#
#       break
#     grid = do_guard_turn(icon, guard_x, guard_y, grid)
#

