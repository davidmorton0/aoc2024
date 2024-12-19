#!/usr/bin/env python

INPUT = 2
FILENAME = ['example.txt', 'input_h.txt', 'input_w.txt'][INPUT]

with open(FILENAME, 'r') as file:
    towel_lines, design_lines = file.read().split("\n\n")

towels = []
for line in towel_lines.split("\n"):
    towels.extend(line.split(", "))

designs = design_lines.split("\n")


def check_for_towel(design_string):
    for towel in towels:
        if design_string == towel:
            return True
        elif design_string[0:len(towel)] == towel:
            if check_for_towel(design_string[len(towel):]):
                return True
    return False

makeable_designs = [design for design in designs if check_for_towel(design)]
print(len(makeable_designs))