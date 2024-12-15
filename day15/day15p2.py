#!/usr/bin/env python
import re
from itertools import batched

filename = 'input.txt'

with open(filename, 'r') as file:
    input = [line for line in file.read().split("\n")]

robot_position = []
map = []
moves = []

def print_map():
    for line in map:
        print(''.join(line))

def move_change(move):
    match move:
        case '<':
            return [- 1, 0]
        case '>':
            return [1, 0]
        case '^':
            return [0, - 1]
        case 'v':
            return [0, 1]

def propose_moves(x, y, move):
    current_symbol = map[y][x]
    change = move_change(move)
    new_x = x + change[0]
    new_y = y + change[1]
    if current_symbol == '[' and move in ['^', 'v']:
        return [
            {
                "current": [x, y],
                "new": [new_x, new_y],
                "current_symbol": map[y][x],
                "new_symbol": map[new_y][new_x]
            },
            {
                "current": [x + 1, y],
                "new": [new_x + 1, new_y],
                "current_symbol": map[y][x + 1],
                "new_symbol": map[new_y][new_x + 1]
            }
        ]
    elif current_symbol == ']' and move in ['^', 'v']:
        return [
            {
                "current": [x, y],
                "new": [new_x, new_y],
                "current_symbol": map[y][x],
                "new_symbol": map[new_y][new_x]
            },
            {
                "current": [x - 1, y],
                "new": [new_x - 1, new_y],
                "current_symbol": map[y][x - 1],
                "new_symbol": map[new_y][new_x - 1]
            }
        ]
    else:
        return [{
            "current": [x, y],
            "new": [new_x, new_y],
            "current_symbol": map[y][x],
            "new_symbol": map[new_y][new_x]
        }]

def do_moves(moves):
    for move in moves[::-1]:
        map[move["current"][1]][move["current"][0]] = '.'
        x, y = move["new"]
        map[y][x] = move["current_symbol"]
    return moves[0]["new"]

def calculate_moves(move, robot_position):
    proposed_moves = propose_moves(*robot_position, move)

    for proposed_move in proposed_moves:
        if proposed_move["new_symbol"] in ['[', ']']:
            proposed_moves.extend(propose_moves(*proposed_move["new"], move))

    new_symbols = [proposed_move["new_symbol"] for proposed_move in proposed_moves]
    if '#' in new_symbols:
        return robot_position
    else:
        return do_moves(proposed_moves)

def count_coordinates(map):
    total = 0
    for y, row in enumerate(map):
        for x, pos in enumerate(list(row)):
            if pos == '[':
                total += 100 * y + x
    return total

get_map = True

chars = {
    '.': '..',
    'O': '[]',
    '#': '##',
    '@': '@.'
}

for y, line in enumerate(input):
    if line == '':
        get_map = False
    if get_map:
        new_line = ''.join([chars[c] for c in list(line)])
        map.append(list(new_line))
    else:
        moves.extend(list(line))

for y, line in enumerate(map):
    if '@' in line:
        robot_position = [line.index('@'), y]


for move in moves:
    robot_position = calculate_moves(move, robot_position)

print_map()
print(count_coordinates(map))
