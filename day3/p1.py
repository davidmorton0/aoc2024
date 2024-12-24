#!/usr/bin/env python
import time
import re

start_time = time.time()

INPUT = 1
FILENAME = ['example_1.txt', 'example_2.txt', 'input_h.txt', 'input_w.txt'][INPUT]
REGEX_1 = r'mul\(\d+,\d+\)'
REGEX_2 = r'mul\((\d+),(\d+)\)'
REGEX_3 = r'^(.*)don\'t\(\).*do\(\)(.*)(don\'t\(\).*)?'

with open(FILENAME, 'r') as file:
    input = file.read()

def process_instruction(instruction):
    numbers = re.match(REGEX_2, instruction)
    return int(numbers[1]) * int(numbers[2])

instructions1 = re.findall(REGEX_1, input)
total = sum([process_instruction(instruction) for instruction in instructions1])

instructions2 = re.match(REGEX_3, input)
print(instructions2.groups())

print("--- %s seconds ---" % (time.time() - start_time))