#!/usr/bin/env python

INPUT = 2
FILENAME = ['example_1.txt', 'input_w.txt', 'input_w.txt'][INPUT]

with open(FILENAME, 'r') as file:
    towel_lines, design_lines = file.read().split("\n\n")

towels = []
for line in towel_lines.split("\n"):
    towels.extend(line.split(", "))

designs = design_lines.split("\n")

towel_permutation_counts = {}

def count_permutations(design_string):
    permutations = 0
    if design_string in towel_permutation_counts:
        return towel_permutation_counts[design_string]
    for towel in towels:
        if design_string == towel:
            permutations += 1
        elif design_string[:len(towel)] == towel:
            permutations += count_permutations(design_string[len(towel):])
    towel_permutation_counts[design_string] = permutations
    return permutations

design_permutations = [count_permutations(design) for design in designs]
print("Part 1")
print(len([c for c in design_permutations if c > 0]))
print("Part 2")
print(sum(design_permutations))