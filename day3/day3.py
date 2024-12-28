#!/usr/bin/env python
import time
import re
from itertools import pairwise

start_time = time.time()

INSTRUCTIONS_REGEX = r'mul\(\d+,\d+\)'
INSTRUCTION_VALUES_REGEX = r'mul\((\d+),(\d+)\)'
ENABLE_DISABLE_REGEX = r'(do\(\)|don\'t\(\))'

def load_input(filename):
    with open(filename, 'r') as file:
        return file.read()

def calculate_instruction_total(instruction):
    numbers = re.match(INSTRUCTION_VALUES_REGEX, instruction)
    return int(numbers[1]) * int(numbers[2])

def calculate_instructions_total(input):
    instructions = re.findall(INSTRUCTIONS_REGEX, input)
    return sum([calculate_instruction_total(instruction) for instruction in instructions])

def calculate_enabled_instructions_total(input):
    split_input = re.split(ENABLE_DISABLE_REGEX, input)
    total = 0
    for part1, part2 in pairwise(['do()', *split_input]):
        if part1 == 'do()':
            total += calculate_instructions_total(part2)
    return total

def solve(filename):
    input = load_input(filename)

    print(calculate_instructions_total(input))
    print(calculate_enabled_instructions_total(input))
    print()

for filename in ['example_1.txt', 'example_2.txt', 'input_w.txt']:
    solve(filename)

print("--- %s seconds ---" % (time.time() - start_time))