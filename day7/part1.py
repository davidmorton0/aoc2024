#!/usr/bin/env python
from itertools import combinations

with open('input.txt', 'r') as file:
    input = file.read().split("\n")

width = len(input[0])
height = len([line for line in input if line != ''])

antennas = {}
for y, line in enumerate(input):
    for x, location in enumerate(list(line)):
        if location != '.':
            coordinates = [x, y]
            if antennas.get(location):
                antennas[location].append(coordinates)
            else:
                antennas[location] = [coordinates]


antenna_combinations = []
for key in antennas.keys():
    antenna_combinations.extend(list(combinations(antennas[key], 2)))

def generate_antinodes(x1, y1, x2, y2):
    return [[2 * x2 - x1, 2 * y2 - y1], [2 * x1 - x2, 2 * y1 - y2]]

def valid_coordinates(x, y):
    return x < width and x >= 0 and y < height and y >= 0

def filter_antinodes(antinodes):
    return [f"{antinode[0]},{antinode[1]}" for antinode in antinodes if valid_coordinates(antinode[0], antinode[1])]

antinodes = []
for [[x1, y1], [x2, y2]] in antenna_combinations:
    antinodes.extend(generate_antinodes(x1, y1, x2, y2))

unique_antinodes = set(filter_antinodes(antinodes))
print(unique_antinodes)
print(len(unique_antinodes))