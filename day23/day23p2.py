#!/usr/bin/env python
from collections import defaultdict
from itertools import combinations
import re

INPUT = 2
FILENAME = ['example.txt', 'example_2.txt', 'input_h.txt', 'input_w.txt'][INPUT]
REGEX = r'(\w\w)-(\w\w)'

with open(FILENAME, 'r') as file:
    connections = [line for line in file.read().split("\n") if line != ""]


computer_connections = defaultdict(lambda : [])
for connection in connections:
    match =  re.match(REGEX, connection)
    computer1 = match[1]
    computer2 = match[2]
    computer_connections[computer1].append(computer2)
    computer_connections[computer2].append(computer1)

def all_computers_connected(computers):
    for a, b in combinations(computers, 2):
        if a not in computer_connections[b]:
            return False
    return True

def find_biggest_group(computers, current_biggest_group):
    if current_biggest_group:
        current_biggest_group_size = len(current_biggest_group)
    else:
        current_biggest_group_size = 3
    print(computers)
    print(current_biggest_group)
    print(list(range(len(computers), current_biggest_group_size, -1)))
    for check_size in range(len(computers), current_biggest_group_size - 1, -1):
        print(check_size)
        for check_computers in combinations(computers, check_size):
            print(check_computers)
            if all_computers_connected(check_computers):
                return check_computers

biggest_group = None
computer_checked = []
for k, v in computer_connections.items():
    check_group = find_biggest_group(v, biggest_group)
    if check_group:
        found_group = list(check_group) + [k]
        found_group.sort()
        print(found_group)
        biggest_group = found_group
    print(len(biggest_group))


print(','.join(biggest_group))

