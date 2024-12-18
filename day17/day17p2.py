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

# program = [0,3,5,4,3,0]
# check_number = 0
# output = []
# REGISTERS = {
#     "A": check_number,
#     "B": 0,
#     "C": 0
# }
# while run_program(program) != program:
#     output = []
#     check_number += 1
#     print(check_number)
#     REGISTERS = {
#         "A": check_number,
#         "B": 0,
#         "C": 0
#     }

def process(a):
    return (((a % 8) ^ 3) ^ int(a / (2 ** ((a % 8) ^ 3))) ^ 3) % 8

RESULTS = []
program = [2,4,1,3,7,5,4,1,1,3,0,3,5,5,3,0]

best = 13513445758112
best = 1
check_numbers = list(range(best, best * 8 + 100000))
# print([best * 8 - 8000, best * 8 + 10000])
for check_number in check_numbers:
    output = []
    REGISTERS = {
        "A": check_number,
        "B": 0,
        "C": 0
    }
    RESULTS.append([check_number, run_program(program), process(check_number)])

digits = 3
check_res = program[-digits:]
correct_results = [result for result in RESULTS if result[1][0] == 2 and result[1][-digits:] == check_res]
print([2,4,1,3,7,5,4,1,1,3,0,3,5,5,3,0][-digits:])
print(correct_results)

'''
1. 2,4 - reg b = reg A mod 8            b = A mod 8
2. 1,3 - reg b = reg b ^ 3              b = (A mod 8) ^ 3 
3. 7,5 - reg c = reg a / 2 ** reg b     c = a/ (2 ** (A mod 8) ^ 3)
4. 4,1 - reg b = reg b ^ reg c          b= ((A mod 8) ^ 3) ^  c)
5. 1,3 - reg b = reg b ^ 3              b = (((A mod 8) ^ 3) ^  c)) ^ 3
6. 0,3 - reg a = reg a / 8              a = a / 8
7. 5,5 - output reg b % 8               output ((((A mod 8) ^ 3) ^  a/ (2 ** (A mod 8) ^ 3))) ^ 3) % 8
8. 3,0 - jump to 0 if reg a not 0
program loops 16 times

if last value is 0
reg b is 8n


'''

