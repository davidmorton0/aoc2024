#!/usr/bin/env python

with open('input.txt', 'r') as file:
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


def print_grid(grid):
    for line in grid:
        print(''.join(line))

for n in list(range(0, 200000)):
    icon, guard_y, guard_x = calculate_guard_position(grid)
    if icon == '*':
      print_grid(grid)
      print('finished')
      print(sum([len([pos for pos in line if pos == 'X']) for line in grid]))

      break
    grid = do_guard_turn(icon, guard_x, guard_y, grid)


