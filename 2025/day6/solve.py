#!/usr/bin/env python
import re
import time
from functools import reduce
from itertools import pairwise
from operator import mul


class Solve:
    def __init__(self):
        self.number_of_lines = None

    def solve_a(self, filename):
        return self.solve(filename, self.construct_problem_a)

    def solve_b(self, filename):
        return self.solve(filename, self.construct_problem_b)
            
    def solve(self, filename, construct_problem):
        print(filename)
        puzzle_input = self.load_input(filename)
        self.number_of_lines = len(puzzle_input)
        problem_starts = self.find_problem_starts(puzzle_input)

        problems = []
        for problem_start, next_problem_start in pairwise(problem_starts):
            problems.append(construct_problem(puzzle_input, problem_start, next_problem_start))
        
        total = sum([self.problem_value(problem) for problem in problems])
        print(total)
        return total

    def load_input(self, filename):
        with open(filename, 'r') as file:
            return file.read().split("\n")
        
    def find_problem_starts(self, puzzle_input):
        problem_starts = []
        for n, character in enumerate(puzzle_input[self.number_of_lines - 1]):
            if character in ["+", "*"]:
                problem_starts.append(n)
        problem_starts.append(len(puzzle_input[0]) + 1)

        return problem_starts

    def construct_problem_a(self, puzzle_input, problem_start, next_problem_start):
        numbers = []
        for n in range(0, self.number_of_lines - 1):
            numbers.append(int(puzzle_input[n][problem_start:next_problem_start - 1]))
        sign = puzzle_input[self.number_of_lines - 1][problem_start]

        return [numbers, sign]

    def construct_problem_b(self, puzzle_input, problem_start, next_problem_start):
        numbers = [[digit] for digit in list(puzzle_input[0][problem_start:next_problem_start - 1])]
        
        for n in range(1, self.number_of_lines - 1):
            for m, number in enumerate(numbers):
                number.append(puzzle_input[n][problem_start + m])
        
        formatted_numbers = [int("".join(number)) for number in numbers]        
        sign = puzzle_input[self.number_of_lines - 1][problem_start]

        return [formatted_numbers, sign]

    def problem_value(self, problem):
        numbers, sign = problem
        if sign == "+":
            return sum(numbers)
        elif sign == "*":
            return reduce(mul, numbers, 1)

start_time = time.time()
print("Part A")
Solve().solve_a('example.txt')
Solve().solve_a('input.txt')
Solve().solve_a('input_2.txt')
print("Part B")
Solve().solve_b('example.txt')
Solve().solve_b('input.txt')
Solve().solve_b('input_2.txt')
print("--- %s seconds ---" % (time.time() - start_time))