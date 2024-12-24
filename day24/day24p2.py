#!/usr/bin/env python
from collections import defaultdict
from operator import itemgetter
import time

start_time = time.time()

INPUT = 2
FILENAME = ['example_1.txt', 'example_2.txt', 'example_3.txt', 'input_h.txt', 'input_w.txt'][INPUT]

with open(FILENAME, 'r') as file:
    initial_wire_values_input, connections_input = file.read().split("\n\n")

def load_initial_values():
    wire_values = defaultdict(lambda : None)
    for line in initial_wire_values_input.split("\n"):
        wire, value = line.split(": ")
        wire_values[wire] = int(value)
    return wire_values

def load_initial_connections():
    connections = []
    for line in connections_input.split("\n"):
        wire1, gate_type, wire2, _, result_wire = line.split(" ")
        connections.append(
            {"wire1": wire1, "wire2": wire2, "gate_type": gate_type, "result_wire": result_wire})
    return connections

def AND(wire1, wire2):
    if wire1 == 1 and wire2 == 1:
        return 1
    return 0

def OR(wire1, wire2):
    if wire1 == 1 or wire2 == 1:
        return 1
    return 0

def XOR(wire1, wire2):
    if wire1 != wire2:
        return 1
    return 0

def get_values(wire_values, start_letter):
    return [[wire, value] for wire, value in wire_values.items() if wire[0] == start_letter]

def check_values(wire_values):
    if (None in get_values(wire_values, 'x') or
        None in get_values(wire_values, 'y') or
        None in get_values(wire_values, 'z')):
        return False
    return True

def calculate_value(wire_values, letter):
    result_values = get_values(wire_values, letter)
    result_values.sort()
    print([letter, result_values])
    return int(''.join([str(result[1]) for result in result_values[::-1]]), 2)

def calculate(wire_values, connections):
    found_result = True
    while found_result:
        found_result = False
        for connection in connections:
            wire1, wire2, gate_type, result_wire = itemgetter("wire1", "wire2", "gate_type", "result_wire")(connection)
            wire_value1 = wire_values[wire1]
            wire_value2 = wire_values[wire2]
            result_value = wire_values[result_wire]
            result = None
            if (not wire_value1 is None) and (not wire_value2 is None) and result_value is None:
                match gate_type:
                    case "AND": result = AND(wire_value1, wire_value2)
                    case "OR": result = OR(wire_value1, wire_value2)
                    case "XOR": result = XOR(wire_value1, wire_value2)
            if result is not None:
                wire_values[result_wire] = result
                found_result = True
    return wire_values

def and_calculation(x, y, z):
    return x & y == z

def check_calculator(swaps):
    wire_values = load_initial_values()
    connections = load_initial_connections()
    for a, b in swaps:
        connections[a]["result_wire"], connections[b]["result_wire"] = connections[b]["result_wire"], connections[a]["result_wire"]
    wire_values_result = calculate(wire_values, connections)

    x = calculate_value(wire_values_result, 'x')
    y = calculate_value(wire_values_result, 'y')
    z = calculate_value(wire_values_result, 'z')
    print(f"Equation: {x} & {y} = {z}")
    print(x & y == z)

    return and_calculation(x, y, z)

print(check_calculator([[0, 5], [1, 2]]))
