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
    rules_input, updates_input = file.read().split("\n\n")

rules = [line.split("|") for line in rules_input.split("\n")]
updates = [line.split(",") for line in updates_input.split("\n")]

def check_update(update):
    valid_update = True
    for rule in rules:
        if rule[0] in update and rule[1] in update and not update.index(rule[0]) < update.index(rule[1]):
            valid_update = False
    return valid_update

def fix_update(update):
    updated = False
    for rule in rules:
        if rule[0] in update and rule[1] in update:
            index1 = update.index(rule[0])
            index2 = update.index(rule[1])
            if index1 > index2:
                update[index1], update[index2] = update[index2], update[index1]
                updated = True
    return updated

correct_total = 0
fixed_total = 0
for update in updates:
    if check_update(update):
        correct_total += int(update[int((len(update) - 1) / 2)])
    else:
        updated = True
        while updated:
            updated = fix_update(update)
        fixed_total += int(update[int((len(update) - 1) / 2)])

print(correct_total)
print(fixed_total)