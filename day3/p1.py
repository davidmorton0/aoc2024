#!/usr/bin/env python
import time
import re
from itertools import pairwise

start_time = time.time()

INPUT = 2
FILENAME = ['example_1.txt', 'example_2.txt', 'input_h.txt', 'input_w.txt'][INPUT]
REGEX_1 = r'mul\(\d+,\d+\)'
REGEX_2 = r'mul\((\d+),(\d+)\)'
REGEX_3 = r'(do\(\)|don\'t\(\))'


with open(FILENAME, 'r') as file:
    input = file.read()

def calculate_instruction_total(instruction):
    numbers = re.match(REGEX_2, instruction)
    return int(numbers[1]) * int(numbers[2])

def calculate_input_total(input):
    instructions = re.findall(REGEX_1, input)
    return sum([calculate_instruction_total(instruction) for instruction in instructions])

instructions_total = calculate_input_total(input)
print(instructions_total)

split_input = re.split(REGEX_3, input)
total = 0
for part1, part2 in pairwise(['do()', *split_input]):
    if part1 == 'do()':
        total += calculate_input_total(part2)
print(total)

print("--- %s seconds ---" % (time.time() - start_time))