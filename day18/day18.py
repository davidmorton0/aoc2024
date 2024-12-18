#!/usr/bin/env python

FILENAME = 'input_h.txt'
SIZE = 71
BYTES_FALLEN = 1024

with open(FILENAME, 'r') as file:
    bytes = [[int(coord) for coord in line.split(',')] for line in file.read().split("\n")]

space = [['.' for col in range(SIZE)] for row in range(SIZE)]



def add_bytes():
    for x, y in bytes[0:BYTES_FALLEN]:
        space[y][x] = '#'

def print_space():
    for row in space:
        print("".join([str(c) for c in row]))

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


add_bytes()
space[0][0] = 0

for n in range(0, 10000):
    do_iteration(n)
    if space[SIZE - 1][SIZE - 1] != '.':
        print(n + 1)
        break


