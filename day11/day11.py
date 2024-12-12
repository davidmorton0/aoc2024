#!/usr/bin/env python
from collections import defaultdict

with open('example.txt', 'r') as file:
    stones = defaultdict(lambda: 0)
    for stone in [int(stone) for stone in file.read().split(' ')]:
        stones[stone] += 1

def blink(stones):
    new_stones = defaultdict(lambda: 0)
    for stone, count in stones.items():
        if stone == 0:
            new_stones[1] += count
        elif has_even_number_of_digits(stone):
            for new_stone in split_digits(stone):
                new_stones[new_stone] += count
        else:
            new_stones[stone * 2024] += count
    return new_stones

def has_even_number_of_digits(stone):
    return len(str(stone)) % 2 == 0

def split_digits(stone):
    stone_string = str(stone)
    mid_position = int(len(stone_string) / 2)
    return [(int(stone_string[0:mid_position])), (int(stone_string[mid_position:]))]

for _ in range(75):
    stones = blink(stones)

print(sum(stones.values()))