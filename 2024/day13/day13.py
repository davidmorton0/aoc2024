#!/usr/bin/env python
import re
from itertools import batched
from time import time

start_time = time()

BUTTON_A_REGEX = r'Button A: X([+-]\d+), Y([+-]\d+)'
BUTTON_B_REGEX = r'Button B: X([+-]\d+), Y([+-]\d+)'
PRIZE_REGEX = r'Prize: X=(\d+), Y=(\d+)'

def load_input(filename):
    with open(filename, 'r') as file:
        lines = [line for line in file.read().split("\n")]

    machines = []
    for machine_lines in batched(lines, 4):
        machines.append({
            "button_a": get_values(BUTTON_A_REGEX, machine_lines[0]),
            "button_b": get_values(BUTTON_B_REGEX, machine_lines[1]),
            "prize": get_values(PRIZE_REGEX, machine_lines[2])
        })
    return machines

def get_values(regex, line):
    match = re.match(regex, line)
    return {"x": int(match[1]), "y": int(match[2])}

def check_value(a_pushes, a, b_pushes, b, prize):
    return a_pushes * a + b_pushes * b == prize

def calculate_tokens(machine, position_adjustment):
    prize_x = machine["prize"]["x"] + position_adjustment
    prize_y = machine["prize"]["y"] + position_adjustment
    a_pushes = int(
        (machine["button_b"]["x"] * prize_y - machine["button_b"]["y"] * prize_x) /
        (machine["button_b"]["x"] * machine["button_a"]["y"] - machine["button_b"]["y"] * machine["button_a"]["x"]))
    b_pushes = int(
        (machine["button_a"]["y"] * prize_x - machine["button_a"]["x"] * prize_y) /
        (machine["button_b"]["x"] * machine["button_a"]["y"] - machine["button_b"]["y"] * machine["button_a"]["x"]))

    if (check_value(a_pushes, machine["button_a"]["x"], b_pushes, machine["button_b"]["x"], prize_x) and
        check_value(a_pushes, machine["button_a"]["y"], b_pushes, machine["button_b"]["y"], prize_y)):
        return 3 * a_pushes + b_pushes
    else:
        return 0

def solve(filename):
    print(f"Filename: {filename}")
    machines = load_input(filename)

    tokens = 0
    for machine in machines:
        tokens += calculate_tokens(machine, 0)
    print(f"Part 1 Tokens needed: {tokens}")

    tokens = 0
    for machine in machines:
        tokens += calculate_tokens(machine, 10000000000000)
    print(f"Part 2 Tokens needed: {tokens}\n")

solve('example.txt')
solve('input.txt')

print("--- %s seconds ---" % (time() - start_time))