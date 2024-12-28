#!/usr/bin/env python
from collections import defaultdict
from itertools import pairwise

INPUT = 0
FILENAME = ['example_1.txt', 'input_w.txt', 'input_w.txt'][INPUT]
PRUNE_NUMBER = 16777216
MAX_SECRET_NUMBERS = 2000

with open(FILENAME, 'r') as file:
    secret_numbers = [int(line) for line in file.read().split("\n") if line != ""]
# secret_numbers = [123]

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

for secret_number in secret_numbers:
    prices = []
    for _ in range(MAX_SECRET_NUMBERS):
        prices.append(int(str(secret_number)[-1]))
        secret_number = calculate_next_secret_number(secret_number)

    price_changes = []
    for m, n in pairwise(prices):
        price_changes.append(n - m)

    price_change_sequences = {}
    for n in range(len(price_changes) - 4):
        price_change_string = ''.join([str(m) for m in price_changes[n:n+4]])
        if price_change_string not in list(price_change_sequences.keys()):
            price_change_sequences[price_change_string] = prices[n+4]

    for pcs, count in price_change_sequences.items():
        price_change_sequences_count[pcs] += count

answer = [[v, k] for k, v in price_change_sequences_count.items()]
answer.sort()
print(answer[-10:])
