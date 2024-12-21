#!/usr/bin/env python
from itertools import pairwise

INPUT = 1
FILENAME = ['example.txt', 'input_h.txt', 'input_w.txt'][INPUT]

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

DIR_PAD_COORDINATES = {
    '<': [0, 0],
    'v': [1, 0],
    '>': [2, 0],
    'EMPTY': [0, 1],
    '^': [1, 1],
    'A': [2, 1],
}


def calculate_presses(current_button, next_button, button_coordinates):
    button_presses = []
    x_dist = button_coordinates[next_button][0] - button_coordinates[current_button][0]
    y_dist = button_coordinates[next_button][1] - button_coordinates[current_button][1]
    if x_dist < 0:
        x_presses = ['<'] * abs(x_dist)
    elif x_dist > 0:
        x_presses = ['>'] * abs(x_dist)
    else:
        x_presses = []
    if y_dist < 0:
        y_presses = ['v'] * abs(y_dist)
    elif y_dist > 0:
        y_presses = ['^'] * abs(y_dist)
    else:
        y_presses = []
    if x_presses and not [button_coordinates[next_button][0], button_coordinates[current_button][1]] == button_coordinates['EMPTY']:
        button_presses.append([*x_presses, *y_presses, 'A'])
    if y_presses and not [button_coordinates[current_button][0], button_coordinates[next_button][1]] == button_coordinates['EMPTY']:
        button_presses.append([*y_presses, *x_presses, 'A'])
    if not (x_presses or y_presses):
        button_presses = [['A']]
    return button_presses


def calculate_sequence_presses(sequence, pad):
    if pad == 'main':
        coordinates = MAIN_PAD_COORDINATES
    else:
        coordinates = DIR_PAD_COORDINATES
    current_button_sequences = calculate_presses('A', sequence[0], coordinates)

    for a, b in pairwise(sequence):
        new_current_button_presses = []
        for current_button_sequence in current_button_sequences:
            for new_button_presses in calculate_presses(a, b, coordinates):
                new_current_button_presses.append(current_button_sequence + new_button_presses)
        current_button_sequences = new_current_button_presses
    return current_button_sequences

def find_numeric_part(sequence):
    return int(''.join([c for c in list(sequence) if c != 'A']))

total = 0
for sequence in sequences:
    print(sequence)
    presses1 = calculate_sequence_presses(sequence, 'main')
    print(presses1)
    presses2 = []
    for presses in presses1:
        presses2.extend(calculate_sequence_presses(presses, 'dir'))
    presses3 = []
    for presses in presses2:
        presses3.extend(calculate_sequence_presses(presses, 'dir'))
    l = min([len(ps) for ps in presses3])
    c = find_numeric_part(sequence)
    print(l)
    print(max([len(ps) for ps in presses3]))
    total += (c * l)
print(total)