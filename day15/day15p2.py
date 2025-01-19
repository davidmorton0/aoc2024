#!/usr/bin/env python
from itertools import chain

FILENAME = 'input.txt'
PART = 1

if PART == 1:
    BOX_GPS_SYMBOL = 'O'
    BOX_SYMBOLS = ['O']
    CONVERT_MAP_CHARS = {
        '.': '.',
        'O': 'O',
        '#': '#',
        '@': '@'
    }
elif PART == 2:
    BOX_GPS_SYMBOL = '['
    BOX_SYMBOLS = ['[', ']']
    CONVERT_MAP_CHARS = {
        '.': '..',
        'O': '[]',
        '#': '##',
        '@': '@.'
    }

MOVE_CHANGES = {
    '<': [- 1, 0],
    '>': [1, 0],
    '^': [0, - 1],
    'v': [0, 1]
}

def print_map():
    for line in map:
        print(''.join(line))

def generate_move(x1, y1, x2, y2, x_adjust):
    return {
        "current": [x1 + x_adjust, y1],
        "new": [x2 + x_adjust, y2],
        "current_symbol": map[y1][x1 + x_adjust],
        "new_symbol": map[y2][x2 + x_adjust]
    }

def propose_moves(x, y, move):
    current_symbol = map[y][x]
    new_x = x + MOVE_CHANGES[move][0]
    new_y = y + MOVE_CHANGES[move][1]
    new_moves = [generate_move(x, y, new_x, new_y, 0)]
    if current_symbol == '[' and move in ['^', 'v']:
        new_moves.append(generate_move(x, y, new_x, new_y, 1))
    elif current_symbol == ']' and move in ['^', 'v']:
        new_moves.append(generate_move(x, y, new_x, new_y, -1))
    return new_moves

def do_moves(moves):
    for move in moves[::-1]:
        map[move["current"][1]][move["current"][0]] = '.'
        x, y = move["new"]
        map[y][x] = move["current_symbol"]

def calculate_moves(move, robot_position):
    proposed_moves = propose_moves(*robot_position, move)

    for proposed_move in proposed_moves:
        if proposed_move["new_symbol"] in BOX_SYMBOLS:
            proposed_moves.extend(propose_moves(*proposed_move["new"], move))
        elif proposed_move["new_symbol"] == '#':
            return robot_position
    do_moves(proposed_moves)
    return proposed_moves[0]["new"]

def count_coordinates(map):
    total = 0
    for y, row in enumerate(map):
        for x, pos in enumerate(list(row)):
            if pos == BOX_GPS_SYMBOL:
                total += 100 * y + x
    return total

def load_map():
    with open(FILENAME, 'r') as file:
        map_lines, moves_lines = file.read().split("\n\n")
    map = []
    for line in map_lines.split("\n"):
        map.append(list(''.join([CONVERT_MAP_CHARS[c] for c in list(line)])))
    moves = list(chain(*[list(line) for line in moves_lines.split("\n")]))

    for y, line in enumerate(map):
        if '@' in line:
            robot_position = [line.index('@'), y]
    return [map, moves, robot_position]

map, moves, robot_position = load_map()

for move in moves:
    robot_position = calculate_moves(move, robot_position)

print(count_coordinates(map))
