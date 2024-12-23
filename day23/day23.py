#!/usr/bin/env python
from collections import defaultdict
from itertools import combinations
import re

INPUT = 1
FILENAME = ['example.txt', 'input_h.txt', 'input_w.txt'][INPUT]
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

print(computer_connections)
list_of_groups = []
for k, v in computer_connections.items():
    for a, b in combinations(v, 2):
        if a in computer_connections[b] and ('t' in [k[0], a[0], b[0]]):
            computers = [k , a, b]
            computers.sort()
            list_of_groups.append(''.join(computers))

unique_connections = set(list_of_groups)
print(unique_connections)
print(len(unique_connections))