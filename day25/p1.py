#!/usr/bin/env python
from collections import defaultdict
from itertools import combinations
import re
import time

start_time = time.time()

INPUT = 1
FILENAME = ['example.txt', 'input_h.txt', 'input_w.txt'][INPUT]
REGEX = r'(\w{2})-(\w{2})'

with open(FILENAME, 'r') as file:
    schematics = file.read().split("\n\n")

def calculate_key_pin_heights(rows):
    pin_heights = []
    for x in range(5):
        spaces = [column[x] for column in rows]
        pin_heights.append(6 - spaces.index('#'))
    return pin_heights

def calculate_lock_pin_heights(rows):
    pin_heights = []
    for x in range(5):
        spaces = [column[x] for column in rows[::-1]]
        pin_heights.append(6 - spaces.index('#'))
    return pin_heights

def does_column_fit(key_height, lock_height):
    return key_height + lock_height < 6

def does_key_fit(key, lock):
    for key_height, lock_height in zip(key, lock):
        if not does_column_fit(key_height, lock_height):
            return False
    return True

keys = []
locks = []
for schematic in schematics:
    rows = schematic.split("\n")
    if rows[0] == '#####':
        locks.append(calculate_lock_pin_heights(rows))
    elif rows[0] == '.....':
        keys.append(calculate_key_pin_heights(rows))

count = 0
for lock in locks:
    for key in keys:
        if does_key_fit(key, lock):
            count += 1
print(count)

# print("--- %s seconds ---" % (time.time() - start_time))
