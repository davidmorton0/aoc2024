#!/usr/bin/env python
from itertools import permutations, chain
from collections import defaultdict

def load_input(filename):
    with open(filename, 'r') as file:
        puzzle_input = [line for line in file.read().split("\n") if line != '']

    width = len(puzzle_input[0])
    height = len(puzzle_input)
    antennas = find_antennas(puzzle_input)

    return width, height, antennas

def find_antennas(input):
    antennas = defaultdict(list)
    antennas.setdefault('missing_key', [])
    for y, line in enumerate(input):
        for x, location in enumerate(list(line)):
            if location != '.':
                coordinates = [x, y]
                antennas[location].append(coordinates)
    return antennas

def generate_antinodes(x1, y1, x2, y2, min_n, max_n, width, height):
    generated_antinodes = []
    for n in range(min_n, max_n + 1):
        x3, y3 = generate_antinode(x1, y1, x2, y2, n)
        if valid_coordinates(x3, y3, width, height):
            generated_antinodes.append([x3, y3])
        else:
            break
    return generated_antinodes

def generate_antinode(x1, y1, x2, y2, n):
    return [x2 + n * (x2 - x1), y2 + n * (y2 - y1)]

def valid_coordinates(x, y, width, height):
    return x in range(width) and y in range(height)

def unique_antinodes(antinodes):
    return set([f"{antinode[0]},{antinode[1]}" for antinode in antinodes])

def antenna_permutations(antennas):
    return list(chain.from_iterable([permutations(antennas[key], 2) for key in antennas.keys()]))

def solve(filename):
    width, height, antennas = load_input(filename)

    part1_antinodes = []
    part2_antinodes = []
    for [[x1, y1], [x2, y2]] in antenna_permutations(antennas):
        part1_antinodes.extend(generate_antinodes(x1, y1, x2, y2, 1, 1, width, height))
        part2_antinodes.extend(generate_antinodes(x1, y1, x2, y2, 0, 1000, width, height))

    print(f"Filename: {filename}")
    print(f"Part 1: {len(unique_antinodes(part1_antinodes))}")
    print(f"Part 2: {len(unique_antinodes(part2_antinodes))}\n")


solve('example.txt')
solve('input.txt')