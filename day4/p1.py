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

rows = [list(row) for row in wordsearch]
columns = [[row[x] for row in rows] for x in range(width)]

down_diagonals = []
for a in range(0 - height + 1, width):
    diagonal = []
    for y in range(height):
        x = a + y
        if x in range(width) and y in range(height):
            diagonal.append(wordsearch[y][x])
    down_diagonals.append(diagonal)

up_diagonals = []
for a in range(0 - height + 1, width):
    diagonal = []
    for b in range(height):
        x = a + b
        y = height - b - 1
        if x in range(width) and y in range(height):
            diagonal.append(wordsearch[y][x])
    up_diagonals.append(diagonal)

REGEX1 = r'XMAS'
REGEX2 = r'SAMX'
def count_xmas(lines):
    return sum(len(re.findall(REGEX1, ''.join(line))) for line in lines) + sum(len(re.findall(REGEX2, ''.join(line))) for line in lines)

lines_col = [rows, columns, up_diagonals, down_diagonals]

xmasses = 0
for lines in lines_col:
    xmasses += count_xmas(lines)
print(xmasses)