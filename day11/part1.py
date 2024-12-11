#!/usr/bin/env python
from collections import defaultdict

with open('input.txt', 'r') as file:
    stones = defaultdict(lambda: 0)
    for stone in [int(stone) for stone in file.read().split("\n")[0].split(' ')]:
        stones[stone] += 1

def blink(stones):
    new_stones = defaultdict(lambda: 0)
    for stone, number in stones.items():
        if stone == 0:
            new_stones[1] += number
        elif len(str(stone)) % 2 == 0:
            str_stone = str(stone)
            mid_position = int(len(str_stone) / 2)
            new_stones[(int(str_stone[0:mid_position]))] += number
            new_stones[(int(str_stone[mid_position:]))] += number
        else:
            new_stones[(int(stone * 2024))] += number
    return new_stones

print(blink(stones))

for n in range(75):
    stones = blink(stones)

print(sum(stones.values()))