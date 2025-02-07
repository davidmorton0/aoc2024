#!/usr/bin/env python

START_COORDINATES = [0,0]

def load_input(filename):
    with open(filename, 'r') as file:
        return file.read()

def solve_p1(input):
    santa_coordinates = process_moves([START_COORDINATES], list(input))
    print_unique_coordinates_count(santa_coordinates)

def solve_p2(input):
    santa_coordinates = process_moves([START_COORDINATES], list(input)[::2])
    robo_santa_coordinates = process_moves([START_COORDINATES], list(input)[1::2])
    print_unique_coordinates_count(santa_coordinates + robo_santa_coordinates)

def process_moves(coordinates, moves):
    [coordinates.append(find_next_coordinates(*coordinates[-1], move)) for move in moves]
    return coordinates

def find_next_coordinates(current_x, current_y, move):
    match move:
        case '<': return [current_x - 1, current_y]
        case '>': return [current_x + 1, current_y]
        case '^': return [current_x, current_y - 1]
        case 'v': return [current_x, current_y + 1]

def print_unique_coordinates_count(coordinates):
    coordinates_strings = [f"{x},{y}" for x, y in coordinates]
    print(len(set(coordinates_strings)))

def solve(filename):
    input = load_input(filename)
    solve_p1(input)
    solve_p2(input)

solve('example.txt')
solve('input.txt')
