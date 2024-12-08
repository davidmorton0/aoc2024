#!/usr/bin/env python
from itertools import permutations, chain
from operator import itemgetter
from collections import defaultdict

def generate_antinode(x1, y1, x2, y2, n):
    return [x2 + n * (x2 - x1), y2 + n * (y2 - y1)]

def generate_antinodes(x1, y1, x2, y2, min_n, max_n):
    generated_antinodes = []
    for n in range(min_n, max_n + 1):
        possible_antinode = generate_antinode(x1, y1, x2, y2, n)
        if valid_coordinates(*possible_antinode):
            generated_antinodes.append(possible_antinode)
        else:
            break
    return generated_antinodes

def valid_coordinates(x, y):
    return x in range(0, width) and y in range(0, height)

def unique_antinodes(antinodes):
    return set([f"{antinode[0]},{antinode[1]}" for antinode in antinodes])

def solve(part):
    antinodes = []
    for [[x1, y1], [x2, y2]] in antenna_permutations:
        if part == 1:
            antinodes.extend(generate_antinodes(x1, y1, x2, y2, 1, 1))
        else:
            antinodes.extend(generate_antinodes(x1, y1, x2, y2, 0, 1000))
    print(len(unique_antinodes(antinodes)))

def find_antennas(input):
    antennas = defaultdict(list)
    antennas.setdefault('missing_key', [])
    for y, line in enumerate(input):
        for x, location in enumerate(list(line)):
            if location != '.':
                coordinates = [x, y]
                antennas[location].append(coordinates)
    return antennas

def calculate_antenna_permutations(antennas):
    return list(chain.from_iterable([permutations(antennas[key], 2) for key in antennas.keys()]))

def load_input(input_file):
    with open(input_file, 'r') as file:
        input = [line for line in file.read().split("\n") if line != '']
    antennas = find_antennas(input)

    return {
        'width': len(input[0]),
        'height': len(input),
        'antenna_permutations': calculate_antenna_permutations(antennas)
    }

input_file = 'input.txt'
width, height, antenna_permutations = itemgetter('width', 'height', 'antenna_permutations')(load_input(input_file))
solve(1)
solve(2)