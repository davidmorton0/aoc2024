#!/usr/bin/env python

FILENAME = 'input_h.txt'

with open(FILENAME, 'r') as file:
    input = [line for line in file.read().split("\n")]

REGISTERS = {
    "A": 0,
    "B": 0,
    "C": 0
}

def process_instruction(instruction, op, output, pointer):
    combo = [0, 1, 2, 3, REGISTERS["A"], REGISTERS["B"], REGISTERS["C"]][op]
    match instruction:
        case 0: REGISTERS["A"] = int(REGISTERS["A"] / 2 ** combo)
        case 1: REGISTERS["B"] = REGISTERS["B"] ^ op
        case 2: REGISTERS["B"] = combo % 8
        case 3:
            if REGISTERS["A"] != 0:
                pointer = op - 2
        case 4: REGISTERS["B"] = REGISTERS["B"] ^ REGISTERS["C"]
        case 5: output.append(combo % 8)
        case 6: REGISTERS["B"] = int(REGISTERS["A"] / 2 ** combo)
        case 7: REGISTERS["C"] = int(REGISTERS["A"] / 2 ** combo)
    pointer += 2
    return output, pointer

def run_program(program):
    pointer = 0
    output = []
    while pointer < len(program):
        output, pointer = process_instruction(program[pointer], program[pointer + 1], output, pointer)
    return output


program = [2,4,1,3,7,5,4,1,1,3,0,3,5,5,3,0]
MAX_DEPTH = 16

def find_output(guess, depth):
    start_range = guess * 8
    end_range = guess * 8 + 8
    results = []
    for check_number in range(start_range, end_range):
        REGISTERS["A"] = check_number
        output = run_program(program)
        results.append([check_number, output])

    for result in results:
        if result[1] == program[-depth:]:
            if depth < MAX_DEPTH:
                find_output(result[0], depth + 1)
            else:
                print(result)

guess = 1
depth = 1
find_output(0, 1)
