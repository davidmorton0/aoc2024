#!/usr/bin/env python
from itertools import pairwise

INPUT = 2
PADS = 25
FILENAME = ['example.txt', 'example_2.txt', 'input_h.txt', 'input_w.txt'][INPUT]

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

DIR_PAD_ROUTES = {
    '<': {
        '<': ['A'],
        'v': ['>', 'A'],
        '>': ['>', '>', 'A'],
        '^': ['^', '>', 'A'],
        'A': ['^', '>', '>', 'A'],
    },
    'v': {
        '<': ['<', 'A'],
        'v': ['A'],
        '>': ['>', 'A'],
        '^': ['^', 'A'],
        'A': ['^', '>', 'A'],
    },
    '>': {
        '<': ['<', '<', 'A'],
        'v': ['<', 'A'],
        '>': ['A'],
        '^': ['<', '^', 'A'],
        'A': ['^', 'A'],
    },
    '^': {
        '<': ['<', 'v', 'A'],
        'v': ['v', 'A'],
        '>': ['>', 'v', 'A'],
        '^': ['A'],
        'A': ['>', 'A'],
    },
    'A': {
        '<': ['<', '<', 'v', 'A'],
        'v': ['<', 'v', 'A'],
        '>': ['v', 'A'],
        '^': ['<', 'A'],
        'A': ['A'],
    }
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

for sequence in sequences:
    print(sequence)
    print(calculate_sequence_presses(sequence, 'main'))
    presses = calculate_sequence_presses(sequence, 'main')[0]

    for _ in range(2):
        presses_needed = []
        current = 'A'
        for press in presses:
            presses_needed.extend(DIR_PAD_ROUTES[current][press])
            current = press
        presses = presses_needed
        print(presses)

press_counts = []
press_count = {}
for k1, v1 in DIR_PAD_ROUTES.items():
    press_count[k1] = {}
    for k2, v2 in v1.items():
        press_count[k1][k2] = len(v2)
press_counts.append(press_count)

print()
for n in range(25):
    press_count = {}
    for k1, v1 in DIR_PAD_ROUTES.items():
        press_count[k1] = {}
        for k2, v2 in v1.items():
            p = ['A', *v2]
            total = 0
            for s, e in pairwise(p):
                total += press_counts[n][s][e]
            # print([k1, k2, v2, total])
            press_count[k1][k2] = total
    press_counts.append(press_count)

print()
print(DIR_PAD_ROUTES)
print()
for p in press_counts:
    print(p)

print()
total = 0
for sequence in sequences:
    print(sequence)
    presses1 = calculate_sequence_presses(sequence, 'main')

    print(presses)
    sequence_total = 99999999999999
    for presses in presses1:
        for _ in range(1):
            presses_needed = []
            current = 'A'
            for press in presses:
                presses_needed.append(press_counts[PADS - 1][current][press])
                current = press
            presses = presses_needed
            print(presses)
            if sum(presses) < sequence_total:
                sequence_total = sum(presses)
    print(sequence_total)
    total += sequence_total * find_numeric_part(sequence)

print(total)
# presses_needed = []
# p1 = {}
# for k, v in DIR_PAD_ROUTES.items():
#     p1[k] = len(v)
# presses_needed.append(p1)


# presses_needed = []
# p1 = {}
# for k, v in DIR_PAD_ROUTES2.items():
#     p1[k] = len(v)
# presses_needed.append(p1)

# for n in range(0, 3):
#     p = {}
#     for k, v in DIR_PAD_ROUTES2.items():
#         p[k] = 0
#         for m in v:
#             p[k] += presses_needed[n][m]
#     presses_needed.append(p)
#
# print(presses1)
# print(presses_needed)
#
# total = 0
# depth = 0
# for p in presses1:
#     total += presses_needed[depth][p]
#
# print(total)

# total = 0
# for sequence in sequences:
#     print(sequence)
#     presses1 = calculate_sequence_presses(sequence, 'main')
#
#     for _ in range(2):
#         presses2 = []
#         for presses in presses1:
#             presses2.extend(calculate_sequence_presses(presses, 'dir'))
#         print(presses2)
#         l = min([len(ps) for ps in presses2])
#         presses1 = [presses for presses in presses2 if len(presses) == l]
#
#
#     l = min([len(ps) for ps in presses2])
#     c = find_numeric_part(sequence)
#     print(c)
#     print(l)
#     total += (c * l)
# print(total)