#!/usr/bin/env python
import time

start_time = time.time()

def load_input(filename):
    with open(filename, 'r') as file:
        rules_input, updates_input = file.read().split("\n\n")

    rules = [line.split("|") for line in rules_input.split("\n")]
    updates = [line.split(",") for line in updates_input.split("\n")]

    return [rules, updates]

def check_update(update, rules):
    for rule in rules:
        if rule[0] in update and rule[1] in update and not update.index(rule[0]) < update.index(rule[1]):
            return False
    return True

def fix_update(update, rules):
    updated = True
    while updated:
        updated = False
        for rule in rules:
            if rule[0] in update and rule[1] in update:
                index1 = update.index(rule[0])
                index2 = update.index(rule[1])
                if index1 > index2:
                    update[index1], update[index2] = update[index2], update[index1]
                    updated = True

def middle_page(update):
    return int(update[int((len(update) - 1) / 2)])

def solve(filename):
    rules, updates = load_input(filename)
    correct_update_total = 0
    fixed_update_total = 0
    for update in updates:
        if check_update(update, rules):
            correct_update_total += middle_page(update)
        else:
            fix_update(update, rules)
            fixed_update_total += middle_page(update)
    print(correct_update_total)
    print(fixed_update_total)
    print()

solve('example.txt')
solve('input.txt')

print("--- %s seconds ---" % (time.time() - start_time))