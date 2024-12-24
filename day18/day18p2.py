#!/usr/bin/env python

INPUT = 2
FILENAME = ['example_1.txt', 'input_w.txt', 'input_h.txt'][INPUT]
SIZE = [7, 71, 71][INPUT]
BYTES_FALLEN = [12, 1024, 1024][INPUT]
MAX_ITERATIONS = 10000

space = [['.' for col in range(SIZE)] for row in range(SIZE)]


with open(FILENAME, 'r') as file:
    bytes = [[int(coord) for coord in line.split(',')] for line in file.read().split("\n")]

def generate_space(space):
    space = [['.' for col in range(SIZE)] for row in range(SIZE)]
    space[0][0] = 0
    return space

def add_bytes(n):
    for x, y in bytes[0:n]:
        space[y][x] = '#'

def convert_space(c):
    if c in ['.', '#']:
        return c
    else:
        return '*'

def print_space():
    for row in space:
        print("".join([convert_space(c) for c in row]))

def update_neighbours(x, y, n):
    coords = [[x + 1, y], [x - 1, y], [x, y + 1], [x, y - 1]]
    for x1, y1 in coords:
        if x1 in range(0, SIZE) and y1 in range(0, SIZE) and space[y1][x1] == ".":
            space[y1][x1] = n

def do_iteration(n):
    for y, row in enumerate(space):
        for x, pos in enumerate(row):
            if pos == n:
                update_neighbours(x, y, n + 1)

def find_path():
    for n in range(0, MAX_ITERATIONS):
        do_iteration(n)
        if space[SIZE - 1][SIZE - 1] != '.':
            return True
    return False

for n in range(2900, len(bytes)):
    space = generate_space(space)
    add_bytes(n)
    if not find_path():
        print("Failed to find path")
        break
    else:
        print(n)
        print("Found")

print(n)
print(bytes[n - 1])
print_space()