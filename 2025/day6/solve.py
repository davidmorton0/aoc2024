#!/usr/bin/env python
import re
import time
from functools import reduce
from operator import mul


class Solve:
    def __init__(self):
        self.total = 0
        self.problems = []

    def solve_a(self, filename):
        input = self.load_input(filename)
        self.process_input(input)
        print(self.problems)

        for problem in self.problems:
            self.process_problem(problem)
        print(self.total)

    def solve_b(self, filename):
        input = self.load_input2(filename)
        self.process_input2(input)
        print(self.problems)
        for problem in self.problems:
            self.process_problem(problem)
        print(self.total)

    def load_input(self, filename):
        with open(filename, 'r') as file:
            return re.split(r'[ ]*\n[ ]*', file.read())

    def load_input2(self, filename):
        with open(filename, 'r') as file:
            return file.read().split("\n")


    def process_input(self, input):
        lines = [[self.process_cell(n) for n in re.split(r'[ ]+', line)] for line in input if line != ""]
        for n in range(0, len(lines[0])):
            self.problems.append([])
        for line in lines:
            for n in range(0, len(lines[0])):
                self.problems[n].append(line[n])

    def process_input2(self, input):
        problems = []
        number_of_lines = len(input)
        blank_string = " " * number_of_lines
        problem = []
        for n in range(0, len(input[0]))[::-1]:
            str = "".join([input[m][n] for m in range(0, number_of_lines)])
            print(str)
            if str == blank_string:
                print("blank")
                problems.append(problem)
                problem = []
                continue
            problem.append(int(str[:-1]))
            print(problem)
            if str[-1] in ["+", "*"]:
                problem.append(str[-1])
        problems.append(problem)
        self.problems = problems
        print(problems)

    def process_cell(self, cell):
        if cell in ["+", "-", "*"]:
            return cell
        return int(cell)

    def process_problem(self, problem):
        numbers = problem[0:-1]
        if problem[-1] == "+":
            self.total += sum(numbers)
        elif problem[-1] == "*":
            self.total += reduce(mul, numbers, 1)









start_time = time.time()
# Solve().solve_a('example.txt')
# Solve().solve_a('input.txt')
print("\n")
# Solve().solve_b('example.txt')
Solve().solve_b('input.txt')
print("--- %s seconds ---" % (time.time() - start_time))