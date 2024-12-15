#!/usr/bin/env python

FILENAME = 'input.txt'
BOX_GPS_SYMBOL = 'O'
MOVE_CHANGES = {
    '<': [- 1, 0],
    '>': [1, 0],
    '^': [0, - 1],
    'v': [0, 1]
}

with open(FILENAME, 'r') as file:
    input = [line for line in file.read().split("\n")]

robot_position = []
map = []
moves = []

def print_map():
    for line in map:
        print(''.join(line))

def propose_moves(x, y, move):
    current_symbol = map[y][x]
    change = MOVE_CHANGES[move]
    new_x = x + change[0]
    new_y = y + change[1]
    new_move = {
        "current": [x, y],
        "new": [new_x, new_y],
        "current_symbol": map[y][x],
        "new_symbol": map[new_y][new_x]
    }
    if current_symbol == '[' and move in ['^', 'v']:
        return [
            new_move,
            {
                "current": [x + 1, y],
                "new": [new_x + 1, new_y],
                "current_symbol": map[y][x + 1],
                "new_symbol": map[new_y][new_x + 1]
            }
        ]
    elif current_symbol == ']' and move in ['^', 'v']:
        return [
            new_move,
            {
                "current": [x - 1, y],
                "new": [new_x - 1, new_y],
                "current_symbol": map[y][x - 1],
                "new_symbol": map[new_y][new_x - 1]
            }
        ]
    else:
        return [new_move]

def do_moves(moves):
    for move in moves[::-1]:
        x, y = move["new"]
        map[y][x] = move["current_symbol"]
    map[moves[0]["current"][1]][moves[0]["current"][0]] = '.'
    return moves[0]["new"]

def calculate_moves(move, robot_position):
    proposed_moves = propose_moves(*robot_position, move)

    for proposed_move in proposed_moves:
        if proposed_move["new_symbol"] == 'O':
            proposed_moves.extend(propose_moves(*proposed_move["new"], move))

    if '#' in [proposed_move["new_symbol"] for proposed_move in proposed_moves]:
        return robot_position
    else:
        return do_moves(proposed_moves)

def count_coordinates(map):
    total = 0
    for y, row in enumerate(map):
        for x, pos in enumerate(list(row)):
            if pos == BOX_GPS_SYMBOL:
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

print(count_coordinates(map))
