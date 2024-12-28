#!/usr/bin/env python

INPUT = 1
FILENAME = ['example_1.txt', 'input_w.txt', 'input_w.txt'][INPUT]
PRUNE_NUMBER = 16777216

with open(FILENAME, 'r') as file:
    secret_numbers = [int(line) for line in file.read().split("\n") if line != ""]

print(secret_numbers)

def mix(number1, number2):
    return number1 ^ number2

def prune(number):
    return number % PRUNE_NUMBER

def calculate_next_secret_number(secret_number):
    sn = prune((mix(secret_number, secret_number * 64)))
    sn = prune(mix(int(sn / 32), sn))
    return prune(mix(sn * 2048, sn))

def calculate_nth_secret_number(sn, n):
    for _ in range(n):
        sn = calculate_next_secret_number(sn)
    return sn

numbers = [calculate_nth_secret_number(sn, 2000) for sn in secret_numbers]
print(sum(numbers))