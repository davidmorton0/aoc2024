#!/usr/bin/env python
from os import times

FILENAME = 'input_h.txt'

with open(FILENAME, 'r') as file:
    input = [line for line in file.read().split("\n")]

REGISTERS = {
    "A": 729,
    "B": 0,
    "C": 0
}

program = [int(n) for n in "0,1,5,4,3,0".split(',')]

def operand(value):
    match value:
        case 0:
            return 0
        case 1:
            return 1
        case 2:
            return 2
        case 3:
            return 3
        case 4:
            return REGISTERS["A"]
        case 5:
            return REGISTERS["B"]
        case 6:
            return REGISTERS["C"]

def process_instruction(instruction, op, pointer=0):
    match instruction:
        case 0:
            return adv(op, pointer)
        case 1:
            return bxl(op, pointer)
        case 2:
            return bst(op, pointer)
        case 3:
            return jnz(op, pointer)
        case 4:
            return bxc(op, pointer)
        case 5:
            return out(op, pointer)
        case 6:
            return bdv(op, pointer)
        case 7:
            return cdv(op, pointer)

def run_program(program):
    pointer = 0
    while pointer < len(program):
        instruction, op = program[pointer:pointer + 2]
        pointer = process_instruction(instruction, op, pointer)
    return output

def adv(op, pointer=0):
    value = int(REGISTERS["A"] / 2 ** operand(op))
    REGISTERS["A"] = value
    return pointer + 2

def bxl(op, pointer=0):
    REGISTERS["B"] = REGISTERS["B"] ^ op
    return pointer + 2

def bst(op, pointer=0):
    REGISTERS["B"] = operand(op) % 8
    return pointer + 2

def jnz(op, pointer=0):
    if REGISTERS["A"] != 0:
        return op
    else:
        return pointer + 2

def bxc(op, pointer=0):
    REGISTERS["B"] = REGISTERS["B"] ^ REGISTERS["C"]
    return pointer + 2

def out(op, pointer=0):
    output.append(operand(op) % 8)
    return pointer + 2

def bdv(op, pointer=0):
    value = int(REGISTERS["A"] / 2 ** operand(op))
    REGISTERS["B"] = value
    return pointer + 2

def cdv(op, pointer=0):
    value = int(REGISTERS["A"] / 2 ** operand(op))
    REGISTERS["C"] = value
    return pointer + 2

program = [2,4,1,3,7,5,4,1,1,3,0,3,5,5,3,0]
best = 1
start_range = best
end_range = best * 8 + 1000
RESULTS = []

for check_number in range(start_range, end_range):
    output = []
    REGISTERS = {
        "A": check_number,
        "B": 0,
        "C": 0
    }
    run_program(program)
    RESULTS.append([check_number, output])

digits = 3
correct_results = [result for result in RESULTS if result[1] == program[-digits:]]
print(program[-digits:])
print(correct_results)
