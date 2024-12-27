#!/usr/bin/env python
from collections import defaultdict
from operator import itemgetter
from itertools import combinations
import time

start_time = time.time()

INPUT = 3
FILENAME = ['example_1.txt', 'example_2.txt', 'example_3.txt', 'input_h.txt', 'input_w.txt'][INPUT]
DIGITS = [3, 5, 6, 45, 45][INPUT]

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
    # print([letter, result_values])
    return int(''.join([str(result[1]) for result in result_values[::-1]]), 2)

def calculate(wire_values, connections):
    found_result = True
    while found_result:
        found_result = False
        for connection in connections:
            wire1, wire2, gate_type, result_wire = itemgetter("wire1", "wire2", "gate_type", "result_wire")(connection)
            wire_value1 = wire_values.get(wire1)
            wire_value2 = wire_values.get(wire2)
            result_value = wire_values.get(result_wire)
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

def plus_calculation(x, y, z):
    return x + y == z

def set_wire_values(x, y):
    wire_values = {}
    for n, val in enumerate(list(bin(x)[2:].zfill(DIGITS))[::-1]):
        wire_values[f"x{str(n).zfill(2)}"] = int(val)
    for n, val in enumerate(list(bin(y)[2:].zfill(DIGITS))[::-1]):
        wire_values[f"y{str(n).zfill(2)}"] = int(val)
    # print(wire_values)
    return wire_values

def check_calculator(swaps, x_values, y_values):
    for x in x_values:
        for y in y_values:
            wire_values = set_wire_values(x, y)
            connections = load_initial_connections()
            for a, b in swaps:
                connections[a]["result_wire"], connections[b]["result_wire"] = connections[b]["result_wire"], connections[a]["result_wire"]
            wire_values_result = calculate(wire_values, connections)

            x = calculate_value(wire_values_result, 'x')
            y = calculate_value(wire_values_result, 'y')
            z = calculate_value(wire_values_result, 'z')
            if not plus_calculation(x, y, z):
                # print(f"Fail: {swaps} {x} + {y} != {z}")
                return False
            # else:
            #     print(f"Success: {x} + {y} = {z}")

    return True

def test(swaps, x_values, y_values, message, should_print):
    if check_calculator(swaps, x_values, y_values):
        if should_print:
            print(f"Success: {message}. Swaps: {swaps}")
        return True
    else:
        if should_print:
            print(f"Failed: {message}. Swaps: {swaps}")
        return False

def passing_tests(swaps, printing, skip_x_values, skip_y_values):
    if not test(swaps, [0], [0], "0 values", printing):
        return False
    for x in range(45):
        if x in skip_x_values:
            continue
        if not test(swaps, [2 ** x], [0], f"x bit {x}", printing):
            return False
    for y in range(45):
        if y in skip_y_values:
            continue
        if not test(swaps, [0], [2 ** y], f"y bit {y}", printing):
            return False
    return True

def count_failing_tests(swaps):
    count = 0
    for x in [38]:
        if not test(swaps, [2 ** x], [0], f"x bit {x}", True):
            count += 1
    for y in [38]:
        if not test(swaps, [0], [2 ** y], f"y bit {y}", True):
            count += 1
    for x in []:
        if not test(swaps, [2 ** x - 1], [1], f"x bit {x}", True):
            count += 1
    return count

def check_swaps(swap_count):
    connections = load_initial_connections()
    for a, b in combinations(range(len(connections)), 2):
        swaps = [[a, b]]
        failing_tests_count = count_failing_tests(swaps)
        if failing_tests_count < swap_count:
            if passing_tests(swaps, False, [5, 11, 23, 38], [5, 11, 23, 38]):
                print(f"Swaps: {swaps}. Failing tests: {failing_tests_count}")
'''
possible swaps
[3, 101] [50, 101] [131, 101] [191, 101] [212, 101] +
[9, 33] [20, 33]
[24, 109] [32, 109] [109, 179] +
[32, 139] +
[41, 74] [108, 74] [177, 74] +
[120, 212] +

[32, 109], [212, 101], [41, 74]
'''
swaps = [[177, 74], [24, 109], [20, 33], [131, 101]]
print(passing_tests(swaps, False, [38], [38]))
print(count_failing_tests([]))
print(count_failing_tests(swaps))
connections = load_initial_connections()
names = []
for a, b in swaps:
    names.append(connections[a]['result_wire'])
    names.append(connections[b]['result_wire'])
    print(connections[a])
    print(connections[b])
names.sort()
print(','.join(names))