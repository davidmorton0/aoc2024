#!/usr/bin/env python

from copy import deepcopy

OPERATIONS = ['+', '*']

with open('example.txt', 'r') as file:
    input = file.read().split("\n")

equations = []

for line in input:
    answer, inputs = line.split(': ')
    equations.append({
        "answer": int(answer),
        "inputs": [int(input) for input in inputs.split(' ')]
    })



def calculate_next_numbers(number, input):
    return [number + input, number * input, int(f"{str(number)}{str(input)}")]

total = 0
for equation in equations:
    answer = equation["answer"]
    start_number = equation["inputs"][0]
    numbers = [start_number]
    for input in equation["inputs"][1:]:
        new_numbers = []
        for number in numbers:
            new_numbers += calculate_next_numbers(number, input)
        numbers = new_numbers
    if answer in numbers:
        total += answer
print(total)
