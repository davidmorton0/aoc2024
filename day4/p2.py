#!/usr/bin/env python
import time

start_time = time.time()

CROSSES = [
    ['A', 'M', 'M', 'S', 'S'],
    ['A', 'S', 'M', 'M', 'S'],
    ['A', 'S', 'S', 'M', 'M'],
    ['A', 'M', 'S', 'S', 'M'],
]

def load_puzzle_input(filename):
    with open(filename, 'r') as file:
        return file.read().split("\n")

def is_xmas_cross(cross):
    return cross in CROSSES

def find_crosses(puzzle_input):
    crosses = []
    for x in range(1, len(puzzle_input[0]) - 1):
        for y in range(1, len(puzzle_input) - 1):
            cross = [
                puzzle_input[y][x],
                puzzle_input[y - 1][x + 1],
                puzzle_input[y + 1][x + 1],
                puzzle_input[y + 1][x - 1],
                puzzle_input[y - 1][x - 1]
            ]
            crosses.append(cross)
    return crosses

def solve(filename):
    puzzle_input = load_puzzle_input(filename)
    crosses = find_crosses(puzzle_input)
    return sum([1 for cross in crosses if is_xmas_cross(cross)])

print(solve('example.txt'))
print()
print(solve('input.txt'))

print("--- %s seconds ---" % (time.time() - start_time))