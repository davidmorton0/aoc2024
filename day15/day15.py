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

def propose_move(x, y, move):
    change = move_change(move)
    new_x = x + change[0]
    new_y = y + change[1]
    return {
        "current": [x, y],
        "new": [new_x, new_y],
        "current_symbol": map[y][x],
        "new_symbol": map[new_y][new_x]
    }

def do_moves(moves):
    for move in moves[::-1]:
        x, y = move["new"]
        map[y][x] = move["current_symbol"]
    map[moves[0]["current"][1]][moves[0]["current"][0]] = '.'
    return moves[0]["new"]

def calculate_moves(move, robot_position):
    proposed_moves = [propose_move(*robot_position, move)]

    while proposed_moves[-1]["new_symbol"] == 'O':
        proposed_moves.append(propose_move(*proposed_moves[-1]["new"], move))
    # print(proposed_moves)

    if proposed_moves[-1]["new_symbol"] == '.':
        return do_moves(proposed_moves)
    return robot_position

def count_coordinates(map):
    total = 0
    for y, row in enumerate(map):
        for x, pos in enumerate(list(row)):
            if pos == 'O':
                total += 100 * y + x
    return total

get_map = True

for y, line in enumerate(input):
    if line == '':
        get_map = False
    if get_map:
        map.append(list(line))
        if '@' in line:
            robot_position = [line.index('@'), y]
    else:
        moves.extend(list(line))

for move in moves:
    robot_position = calculate_moves(move, robot_position)
    # print(robot_position)
    # print(move)
    # print_map()

print(count_coordinates(map))
