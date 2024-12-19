#!/usr/bin/env python

INPUT = 1
FILENAME = ['example.txt', 'input_h.txt', 'input_w.txt'][INPUT]

with open(FILENAME, 'r') as file:
    towel_lines, design_lines = file.read().split("\n\n")

towels = []
for line in towel_lines.split("\n"):
    towels.extend(line.split(", "))

designs = design_lines.split("\n")
design_counts = {}

def count_combinations(design_string):
    combinations = 0
    if design_string in design_counts:
        return design_counts[design_string]
    for towel in towels:
        if design_string == towel:
            combinations += 1
        elif design_string[0:len(towel)] == towel:
            combinations += count_combinations(design_string[len(towel):])
    design_counts[design_string] = combinations
    return combinations

# def check_for_towel(design_string):
#     if design_string in design_count:
#         return design_count[design_string]
#     for towel in towels:
#         if design_string == towel:
#             return 1
#         elif design_string[0:len(towel)] == towel:
#             check_for_towel(design_string[len(towel):])
#
#     return False

# print(f"Designs: {len(designs)}")
# for n, design in enumerate(designs):
#     print(n)
# check_for_towel(designs[0])

print(sum([count_combinations(design) for design in designs]))