#!/usr/bin/env python
from collections import defaultdict
from operator import itemgetter
import time

start_time = time.time()

INPUT = 3
FILENAME = ['example_1.txt', 'example_2.txt', 'input_h.txt', 'input_w.txt'][INPUT]
REGEX = r'(\w{2})-(\w{2})'

with open(FILENAME, 'r') as file:
    initial_wire_values_input, connections_input = file.read().split("\n\n")

wire_values = defaultdict(lambda : None)
for line in initial_wire_values_input.split("\n"):
    wire, value = line.split(": ")
    wire_values[wire] = int(value)

connections = []
for line in connections_input.split("\n"):
    wire1, gate_type, wire2, _, result_wire = line.split(" ")
    connections.append(
        {"wire1": wire1, "wire2": wire2, "gate_type": gate_type, "result_wire": result_wire})

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

def calculate_result():
    z_results = [[wire, value] for wire, value in wire_values.items() if wire[0] == 'z']
    z_results.sort()
    binary_result = ''.join([str(result[1]) for result in z_results[::-1]])
    return int(binary_result, 2)

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


print(calculate_result())
