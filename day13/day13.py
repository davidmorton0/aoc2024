#!/usr/bin/env python
import re
from itertools import batched

with open('input.txt', 'r') as file:
    lines = [line for line in file.read().split("\n")]

machines = []
for machine in batched(lines, 4):
    match = re.match(r'Button A: X([+-]\d+), Y([+-]\d+)', machine[0])
    button_a = {"x": int(match[1]), "y": int(match[2])}
    match = re.match(r'Button B: X([+-]\d+), Y([+-]\d+)', machine[1])
    button_b = {"x": int(match[1]), "y": int(match[2])}
    match = re.match(r'Prize: X=(\d+), Y=(\d+)', machine[2])
    prize = {"x": int(match[1]), "y": int(match[2])}
    machines.append({"button_a": button_a, "button_b": button_b, "prize": prize})

def check_value(a_pushes, a, b_pushes, b, prize):
    return a_pushes * a["x"] + b_pushes * b["x"] == prize["x"] and a_pushes * a["y"] + b_pushes * b["y"] == prize["y"]

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
    if check_value(a_pushes, machine["button_a"], b_pushes, machine["button_b"], machine["prize"]):
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