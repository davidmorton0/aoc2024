#!/usr/bin/env python

from collections import defaultdict

def load_input(filename):
    with open(filename, 'r') as file:
        return file.read()

def solve_p1(input):
    print(input.count('(') - input.count(')'))

def solve_p2(input):
    brackets = defaultdict(lambda : 0)
    for n, bracket in enumerate(list(input)):
        brackets[bracket] += 1
        if brackets[')'] > brackets['(']:
            print(n + 1)
            return

def solve(filename):
    input = load_input(filename)
    solve_p1(input)
    solve_p2(input)


solve('example.txt')
solve('input.txt')