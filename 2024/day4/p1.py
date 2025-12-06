#!/usr/bin/env python
import time
import re

start_time = time.time()

def load_puzzle_input(filename):
    with open(filename, 'r') as file:
        return file.read().split("\n")

def find_rows(puzzle_input):
    return [list(row) for row in puzzle_input]

def find_columns(rows, width):
    return [[row[x] for row in rows] for x in range(width)]

def find_down_diagonals(puzzle_input, height, width):
    diagonals = []
    for a in range(0 - height + 1, width):
        diagonal = []
        for y in range(height):
            x = a + y
            if x in range(width) and y in range(height):
                diagonal.append(puzzle_input[y][x])
        diagonals.append(diagonal)
    return diagonals

def find_up_diagonals(puzzle_input, height, width):
    diagonals = []
    for a in range(0 - height + 1, width):
        diagonal = []
        for b in range(height):
            x = a + b
            y = height - b - 1
            if x in range(width) and y in range(height):
                diagonal.append(puzzle_input[y][x])
        diagonals.append(diagonal)
    return diagonals

def find_lines(puzzle_input, height, width):
    rows = find_rows(puzzle_input)
    columns = find_columns(rows, width)
    up_diagonals = find_up_diagonals(puzzle_input, height, width)
    down_diagonals = find_down_diagonals(puzzle_input, height, width)

    return [rows, columns, up_diagonals, down_diagonals]

def count_xmassess_in_line(line):
    return len(re.findall(r'XMAS', ''.join(line)))

def count_xmasses(lines):
    return sum(count_xmassess_in_line(line) + count_xmassess_in_line(line[::-1]) for line in lines)

def solve(filename):
    puzzle_input = load_puzzle_input(filename)
    width = len(puzzle_input[0])
    height = len(puzzle_input)

    return sum(count_xmasses(lines) for lines in find_lines(puzzle_input, height, width))

print(solve('example.txt'))
print()
print(solve('input.txt'))

print("--- %s seconds ---" % (time.time() - start_time))