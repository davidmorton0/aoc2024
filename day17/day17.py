#!/usr/bin/env python

FILENAME = 'input.txt'

with open(FILENAME, 'r') as file:
    input = [line for line in file.read().split("\n")]

register_a = 729
register_b = 0
register_c = 0

program = [int(n) for n in "0,1,5,4,3,0".split(',')]


print(program)

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
            return register_a
        case 5:
            return register_b
        case 6:
            return register_c


def adv(value):
    return int(register_a / 2 ** operand(value))

def bxl(value):
