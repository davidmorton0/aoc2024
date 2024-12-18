#!/usr/bin/env python

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
        # print([pointer, [instruction, op]])
        pointer = process_instruction(instruction, op, pointer)
        # print(output)
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

# Tests

REGISTERS["A"] = 8
assert adv(2) == 2
assert REGISTERS["A"] == 2

REGISTERS["A"] = 32
REGISTERS["B"] = 3
assert adv(5) == 2
assert REGISTERS["A"] == 4

REGISTERS["A"] = 8
assert process_instruction(0, 2) == 2
assert REGISTERS["A"] == 2

REGISTERS["B"] = 1
assert bxl(5) == 2
assert REGISTERS["B"] == 4

REGISTERS["B"] = 2
assert bxl(5) == 2
assert REGISTERS["B"] == 7

REGISTERS["A"] = 11
REGISTERS["B"] = 0
assert bst(1) == 2
assert REGISTERS["B"] == 1
assert bst(4) == 2
assert REGISTERS["B"] == 3

assert jnz(1) == 1
assert jnz(9) == 9

REGISTERS["B"] = 1
REGISTERS["C"] = 2
assert bxc(7) == 2
assert REGISTERS["B"] == 3

output = []
REGISTERS["A"] = 8
REGISTERS["B"] = 17
assert out(1) == 2
assert out(2) == 2
assert out(4) == 2
assert out(5) == 2
assert output == [1, 2, 0, 1]

REGISTERS["A"] = 8
assert bdv(2) == 2
assert REGISTERS["B"] == 2

REGISTERS["A"] = 32
REGISTERS["B"] = 3
assert bdv(5) == 2
assert REGISTERS["B"] == 4

REGISTERS["A"] = 8
assert process_instruction(6, 2) == 2
assert REGISTERS["B"] == 2



REGISTERS["A"] = 8
assert cdv(2) == 2
assert REGISTERS["C"] == 2

REGISTERS["A"] = 32
REGISTERS["B"] = 3
assert cdv(5) == 2
assert REGISTERS["C"] == 4

REGISTERS["A"] = 8
assert process_instruction(7, 2) == 2
assert REGISTERS["C"] == 2

# Program tests
REGISTERS = {
        "A": 0,
        "B": 0,
        "C": 9
}
run_program([2, 6])
assert REGISTERS["B"] == 1

output = []
REGISTERS = {
        "A": 10,
        "B": 0,
        "C": 0
}
assert run_program([5,0,5,1,5,4]) == [0, 1, 2]

output = []
REGISTERS = {
        "A": 2024,
        "B": 0,
        "C": 0
}
assert run_program([0,1,5,4,3,0]) == [4,2,5,6,7,7,7,7,3,1,0]
assert REGISTERS["A"] == 0

output = []
REGISTERS = {
        "A": 0,
        "B": 29,
        "C": 0
}
assert run_program([1,7]) == []
assert REGISTERS["B"] == 26

output = []
REGISTERS = {
        "A": 0,
        "B": 2024,
        "C": 43690
}
assert run_program([4,0]) == []
assert REGISTERS["B"] == 44354

# Test input
REGISTERS = {
    "A": 729,
    "B": 0,
    "C": 0
}
print(program)
print(",".join([str(c) for c in run_program(program)]))

output = []
REGISTERS = {
    "A": 37283687,
    "B": 0,
    "C": 0
}
program = [2,4,1,3,7,5,4,1,1,3,0,3,5,5,3,0]
print(program)
print(",".join([str(c) for c in run_program(program)]))

output = []
REGISTERS = {
    "A": 117440,
    "B": 0,
    "C": 0
}
program = [0,3,5,4,3,0]
print(program)
print(",".join([str(c) for c in run_program(program)]))


program = [0,3,5,4,3,0]
check_number = 0
output = []
REGISTERS = {
    "A": check_number,
    "B": 0,
    "C": 0
}
while run_program(program) != program:
    output = []
    check_number += 1
    print(check_number)
    REGISTERS = {
        "A": check_number,
        "B": 0,
        "C": 0
    }
