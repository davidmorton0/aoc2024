#!/usr/bin/env python
import time
import re

start_time = time.time()

INPUT = 1
FILENAME = ['example.txt', 'input_h.txt', 'input_w.txt'][INPUT]

with open(FILENAME, 'r') as file:
    wordsearch = file.read().split("\n")

width = len(wordsearch[0])
height = len(wordsearch)

crosses = []
for x in range(1, width - 1):
    for y in range(1, height -1):
        cross = [
            wordsearch[y][x],
            wordsearch[y - 1][x + 1],
            wordsearch[y + 1][x + 1],
            wordsearch[y + 1][x - 1],
            wordsearch[y - 1][x - 1]
        ]
        crosses.append(cross)

CROSSES = [
    ['A', 'M', 'M', 'S', 'S'],
    ['A', 'S', 'M', 'M', 'S'],
    ['A', 'S', 'S', 'M', 'M'],
    ['A', 'M', 'S', 'S', 'M'],
]

def is_cross(cross):
    return cross in CROSSES

print(sum([1 for cross in crosses if is_cross(cross)]))