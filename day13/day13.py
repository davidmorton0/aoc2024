#!/usr/bin/env python
import re
from itertools import batched

BUTTON_A_REGEX = r'Button A: X([+-]\d+), Y([+-]\d+)'
BUTTON_B_REGEX = r'Button B: X([+-]\d+), Y([+-]\d+)'
PRIZE_REGEX = r'Prize: X=(\d+), Y=(\d+)'

with open('input.txt', 'r') as file:
    lines = [line for line in file.read().split("\n")]

def get_values(regex, line):
    match = re.match(regex, line)
    return {"x": int(match[1]), "y": int(match[2])}

machines = []
for machine_lines in batched(lines, 4):
    machines.append({
        "button_a": get_values(BUTTON_A_REGEX, machine_lines[0]),
        "button_b": get_values(BUTTON_B_REGEX, machine_lines[1]),
        "prize": get_values(PRIZE_REGEX, machine_lines[2])
    })

def check_value(a_pushes, a, b_pushes, b, prize):
    return a_pushes * a + b_pushes * b == prize

def check_values(a_pushes, a, b_pushes, b, prize):
    return (check_value(a_pushes, a["x"], b_pushes, b["x"], prize["x"]) and
            check_value(a_pushes, a["y"], b_pushes, b["y"], prize["y"]))

def calculate_tokens(machine):
    m_1 = machine["button_b"]["x"] * machine["button_a"]["y"]
    t_1 = machine["button_b"]["x"] * machine["prize"]["y"]

    m_2 = machine["button_b"]["y"] * machine["button_a"]["x"]
    t_2 = machine["button_b"]["y"] * machine["prize"]["x"]

    m_3 = machine["button_b"]["x"] * machine["button_a"]["y"]
    t_3 = machine["button_a"]["y"] * machine["prize"]["x"]

    m_4 = machine["button_b"]["y"] * machine["button_a"]["x"]
    t_4 = machine["button_a"]["x"] * machine["prize"]["y"]

    a_pushes = int((t_1 - t_2) / (m_1 - m_2))
    b_pushes = int((t_3 - t_4) / (m_3 - m_4))
    if check_values(a_pushes, machine["button_a"], b_pushes, machine["button_b"], machine["prize"]):
        return (3 * a_pushes + b_pushes)
    else:
        return 0

tokens = 0
for machine in machines:
    tokens += calculate_tokens(machine)
print(tokens)

tokens = 0
for machine in machines:
    machine["prize"]["x"] += 10000000000000
    machine["prize"]["y"] += 10000000000000
    tokens += calculate_tokens(machine)
print(tokens)