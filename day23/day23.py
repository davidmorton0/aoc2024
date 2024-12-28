#!/usr/bin/env python
from collections import defaultdict
from itertools import combinations
import re
import time

start_time = time.time()

INPUT = 2
FILENAME = ['example_1.txt', 'example_2.txt', 'input.txt', 'input_w.txt'][INPUT]
REGEX = r'(\w{2})-(\w{2})'


with open(FILENAME, 'r') as file:
    connection_list = [line for line in file.read().split("\n") if line != ""]

def find_connections_by_computer(connection_list):
    connections = defaultdict(lambda : [])
    for connection in connection_list:
        match =  re.match(REGEX, connection)
        computer1 = match[1]
        computer2 = match[2]
        connections[computer1].append(computer2)
        connections[computer2].append(computer1)
    return connections

def all_computers_connected(computers):
    for computer1, computer2 in combinations(computers, 2):
        if computer1 not in connections[computer2]:
            return False
    return True

def find_network_with_size(computers, network_size):
    for computers_to_check in combinations(computers, network_size):
        if all_computers_connected(computers_to_check):
            return computers_to_check

def find_larger_network(computers, largest_network_found_size):
    for network_size in range(len(computers), largest_network_found_size - 1, -1):
        network = find_network_with_size(computers, network_size)
        if network:
            return network

def find_networks_with_3_computers_and_t_computer():
    list_of_groups = []
    for computer1, connected_computers in connections.items():
        if computer1[0] != 't':
            continue
        for computer2, computer3 in combinations(connected_computers, 2):
            if computer2 in connections[computer3]:
                computers = [computer1, computer2, computer3]
                computers.sort()
                list_of_groups.append(''.join(computers))
    return len(set(list_of_groups))

def find_largest_network():
    largest_network_found = []
    for computer, connected_computers in connections.items():
        network_found = find_larger_network(connected_computers, len(largest_network_found))
        if network_found:
            largest_network_found = [*network_found, computer]
    largest_network_found.sort()
    return largest_network_found

connections = find_connections_by_computer(connection_list)
print(find_networks_with_3_computers_and_t_computer())
print(','.join(find_largest_network()))
print("--- %s seconds ---" % (time.time() - start_time))
