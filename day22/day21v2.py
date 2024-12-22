#!/usr/bin/env python
from itertools import pairwise
from collections import defaultdict

INPUT = 2
FILENAME = ['example_1.txt', 'example_2.txt', 'input_h.txt', 'input_w.txt'][INPUT]
PRUNE_NUMBER = 16777216
MAX_SECRET_NUMBERS = 2000

with open(FILENAME, 'r') as file:
    secret_numbers = [int(line) for line in file.read().split("\n") if line != ""]

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

price_change_sequences_count = defaultdict(lambda: 0)
secret_numbers_total = 0
for secret_number in secret_numbers:
    prices = []
    price_changes = []
    price_change_sequences = []
    for _ in range(MAX_SECRET_NUMBERS):
        prices.append(secret_number % 10)
        if len(prices) >= 2:
            price_changes.append(prices[-1] - prices[-2])
        if len(prices) >= 4:
            price_change_string = ''.join([str(m) for m in price_changes[-4:]])
            if price_change_string not in price_change_sequences:
                price_change_sequences.append(price_change_string)
                price_change_sequences_count[price_change_string] += prices[-1]
        secret_number = calculate_next_secret_number(secret_number)
    secret_numbers_total += secret_number

answer = [[v, k] for k, v in price_change_sequences_count.items()]
answer.sort()
print(secret_numbers_total)
print(answer[-10:])
