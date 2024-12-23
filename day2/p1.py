#!/usr/bin/env python
import time
from itertools import pairwise

start_time = time.time()

INPUT = 1
FILENAME = ['example.txt', 'input_h.txt', 'input_w.txt'][INPUT]

with open(FILENAME, 'r') as file:
    reports = []
    for line in file.read().split("\n"):
        if line == "":
            continue
        reports.append([int(levels) for levels in line.split(" ")])

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

safe_reports = [report for report in reports if is_safe(report)]
print(len(safe_reports))
safe_reports = [report for report in reports if is_safe(report) or is_safe_with_problem_damper(report)]
print(len(safe_reports))

print("--- %s seconds ---" % (time.time() - start_time))