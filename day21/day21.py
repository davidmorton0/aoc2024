#!/usr/bin/env python
from itertools import pairwise
from math import inf

INPUT = 1
PADS = 25
FILENAME = ['example_1.txt', 'input_h.txt', 'input_w.txt'][INPUT]

with open(FILENAME, 'r') as file:
    sequences = [list(line) for line in file.read().split("\n") if line != ""]

MAIN_PAD_COORDINATES = {
    'EMPTY': [0,0],
    '0': [1, 0],
    'A': [2, 0],
    '1': [0, 1],
    '2': [1, 1],
    '3': [2, 1],
    '4': [0, 2],
    '5': [1, 2],
    '6': [2, 2],
    '7': [0, 3],
    '8': [1, 3],
    '9': [2, 3],
}

DIR_PAD_ROUTES = {
    '<': {
        '<': ['A'],
        'v': ['>', 'A'],
        '>': ['>', '>', 'A'],
        '^': ['>', '^', 'A'],
        'A': ['>', '>', '^','A'],
    },
    'v': {
        '<': ['<', 'A'],
        'v': ['A'],
        '>': ['>', 'A'],
        '^': ['^', 'A'],
        'A': [ '^', '>','A'],
    },
    '>': {
        '<': ['<', '<', 'A'],
        'v': ['<', 'A'],
        '>': ['A'],
        '^': ['<', '^', 'A'],
        'A': ['^', 'A'],
    },
    '^': {
        '<': ['v', '<', 'A'],
        'v': ['v', 'A'],
        '>': [ 'v','>', 'A'],
        '^': ['A'],
        'A': ['>', 'A'],
    },
    'A': {
        '<': ['v', '<', '<', 'A'],
        'v': ['<', 'v', 'A'],
        '>': ['v', 'A'],
        '^': ['<', 'A'],
        'A': ['A'],
    }
}
def calculate_sequence_presses(sequence):
    moves_list = [[]]
    start_x, start_y = MAIN_PAD_COORDINATES['A']
    for button in sequence:
        x, y = MAIN_PAD_COORDINATES[button]
        x_diff = x - start_x
        x_moves = ['>'] * x_diff + ['<'] * -x_diff
        y_diff = y - start_y
        y_moves = ['^'] * y_diff + ['v'] * -y_diff
        possible_moves = []
        if not(start_y == 0 and x == 0) and y_diff != 0:
            possible_moves.append(x_moves + y_moves + ['A'])
        if not(start_x == 0 and y == 0) and x_diff != 0:
            possible_moves.append(y_moves + x_moves + ['A'])
        start_x, start_y = x, y

        m = []
        for moves in moves_list:
            for p in possible_moves:
                m.append(moves + p)
        moves_list = m
    return moves_list

def find_numeric_part(sequence):
    return int(''.join(sequence[:-1]))

def generate_button_press_counts(press_counts):
    for n in range(PADS - 1):
        press_count = {}
        for k1, v1 in DIR_PAD_ROUTES.items():
            press_count[k1] = {}
            for k2, v2 in v1.items():
                p = ['A', *v2]
                total = 0
                for s, e in pairwise(p):
                    total += press_counts[n][s][e]
                press_count[k1][k2] = total
        press_counts.append(press_count)

press_count = {}
for k1, v1 in DIR_PAD_ROUTES.items():
    press_count[k1] = {}
    for k2, v2 in v1.items():
        press_count[k1][k2] = len(v2)

press_counts = [press_count]
generate_button_press_counts(press_counts)

total2 = 0
total = 0
for sequence in sequences:
    sequence_total2 = inf
    sequence_total = inf
    for presses in calculate_sequence_presses(sequence):
        presses_needed2 = []
        presses_needed = []
        current = 'A'
        for press in presses:
            presses_needed2.append(press_counts[1][current][press])
            presses_needed.append(press_counts[PADS - 1][current][press])
            current = press
        if sum(presses_needed) < sequence_total:
            sequence_total = sum(presses_needed)
        if sum(presses_needed2) < sequence_total2:
            sequence_total2 = sum(presses_needed2)

    # print(sequence)
    # print(sequence_total)
    numeric = find_numeric_part(sequence)
    total2 += sequence_total2 * numeric
    total += sequence_total * numeric

print(total2)
print(total)
