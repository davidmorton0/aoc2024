#!/usr/bin/env python
import time

start_time = time.time()

OPERATIONS = ['+', '*']

def parse_line(line):
    answer, values = line.split(': ')
    return {
        "answer": int(answer),
        "values": [int(puzzle_input) for puzzle_input in values.split(' ')]
    }

def load_input(filename):
    with open(filename, 'r') as file:
        puzzle_input = file.read().split("\n")
    return [parse_line(line) for line in puzzle_input]

def calculate_next_answers(answer, value, part):
    answers = []
    if answer > value:
        answers.append(answer - value)
    if answer % value == 0:
       answers.append(int(answer / value))
    if part == '2' and ends_with_value(value, answer):
        answers.append(answer_without_value(answer, value))
    return answers

def ends_with_value(value, answer):
    return answer > value and str(answer).endswith(str(value))

def answer_without_value(answer, value):
    return int(str(answer)[0:-len(str(value))])

def check_equation(equation, part):
    answers = [equation["answer"]]
    for value in equation["values"][:0:-1]:
        new_answers = []
        for answer in answers:
            new_answers.extend(calculate_next_answers(answer, value, part))
        answers = new_answers
    return equation["values"][0] in answers

def calculate_equations_total(equations, part):
    return sum([equation["answer"] for equation in equations if check_equation(equation, part)])

def solve(filename):
    equations = load_input(filename)
    part_1_total = calculate_equations_total(equations, '1')
    part_2_total = calculate_equations_total(equations, '2')
    print(f"Filename: {filename}")
    print(f"Part 1: {part_1_total}")
    print(f"Part 1: {part_2_total}\n")

solve('example.txt')
solve('input.txt')

print("--- %s seconds ---" % (time.time() - start_time))