#!/usr/bin/env python
import time

start_time = time.time()

def load_input(filename):
    with open(filename, 'r') as file:
        schematics = file.read().split("\n\n")
    keys = []
    locks = []
    for schematic in schematics:
        rows = schematic.split("\n")
        if rows[0] == '#####':
            locks.append(calculate_pin_heights(rows[::-1]))
        elif rows[0] == '.....':
            keys.append(calculate_pin_heights(rows))
    return [keys, locks]

def calculate_pin_heights(rows):
    pin_heights = []
    for x in range(5):
        spaces = [column[x] for column in rows]
        pin_heights.append(6 - spaces.index('#'))
    return pin_heights

def does_column_fit(key_height, lock_height):
    return key_height + lock_height < 6

def does_key_fit(key, lock):
    for key_height, lock_height in zip(key, lock):
        if not does_column_fit(key_height, lock_height):
            return False
    return True

def solve(filename):
    keys, locks =  load_input(filename)

    count = 0
    for lock in locks:
        count += sum([1 for key in keys if does_key_fit(key, lock)])
    print(count)

solve('example.txt')
solve('input_h.txt')
solve('input_w.txt')

print("--- %s seconds ---" % (time.time() - start_time))
