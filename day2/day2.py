#!/usr/bin/env python
import time
from itertools import pairwise

start_time = time.time()

def load_input(filename):
    with open(filename, 'r') as file:
        reports = []
        for line in file.read().split("\n"):
            if line == "":
                continue
            reports.append([int(levels) for levels in line.split(" ")])
    return reports

def is_safe(report):
    if report[0] == report[1]:
        return False
    allowed_range = range(1, 4) if report[0] < report[1] else range(-1, -4, -1)

    for level1, level2 in pairwise(report):
        if level2 - level1 not in allowed_range:
            return False
    return True

def is_safe_with_problem_damper(report):
    for removed_level in range(0, len(report)):
        if is_safe(report[:removed_level] + report[removed_level + 1:]):
            return True
    return False

def solve(filename):
    reports = load_input(filename)
    print(len([report for report in reports if is_safe(report)]))
    print(len([report for report in reports if is_safe(report) or is_safe_with_problem_damper(report)]))
    print()

solve('example.txt')
solve('input.txt')

print("--- %s seconds ---" % (time.time() - start_time))