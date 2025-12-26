#!/usr/bin/env python
import time
from math import inf, floor
from fractions import Fraction

VERBOSE = False

class Solve:
    def __init__(self):
        self.machines = []

    def load_input(self, filename):
        with open(filename, 'r') as file:
            input = file.read().split("\n")

        for line in input:
            machine_line = line.split(" ")
            buttons = [[int(b) for b in button[1:-1].split(",")] for button in machine_line[1:-1]]
            machine = {
                "lights": machine_line[0][1:-1],
                "buttons": buttons,
                "joltage": [int(j) for j in machine_line[-1][1:-1].split(",")]
            }
            self.machines.append(machine)
        print(self.machines)


    def solve_a(self, filename):
        self.load_input(filename)
        total = 0
        for machine in self.machines:
            count = self.calculate_presses(machine)
            print(count)
            total += count
        print(total)
    
    def calculate_presses(self, machine):
        final_lights = machine["lights"]
        buttons = machine["buttons"]
        states = self.generate_state(len(buttons))
        lowest = None
        for state in states:
            lights_state = len(final_lights) * "."
            for n in range(0, len(state)):
                if state[n] == "1":
                    lights_state = self.press_button(buttons[n], lights_state)
            if lights_state == final_lights:
                button_presses = sum([int(i) for i in list(state)])
                if lowest is None or button_presses < lowest:
                    lowest = button_presses
        return lowest
                 
    
    def generate_state(self, length):
        states = []
        for i in range(0, 2 ** length):
            states.append(str(bin(i))[2:].rjust(length, '0'))
        return states
            
    
    def press_button(self, button, current_lights):
        lights = list(current_lights)
        for button_change in button:
            lights[button_change] = self.flip_light(lights[button_change])
        return "".join(lights)
    
    def flip_light(self, current_state):
        if current_state == ".":
            return "#"
        return "."
        

    def solve_b(self, filename):
        self.load_input(filename)
        start_machine = 0
        end_machine = -1
        total = 0
        for machine_number, machine in enumerate(self.machines[start_machine:end_machine]):
            print(f"Starting machine: {machine_number}")
            joltage = machine["joltage"]
            buttons = machine["buttons"]
            number_of_buttons = len(buttons)
            joltage_length = len(joltage)
            
            equations = self.calculate_equations(buttons, joltage)
            equations.sort(reverse=True)
            if VERBOSE:
                print("Calculate equations")
            self.print_equations(equations)
            pivots = []
            free_values = []
            start_y = 0
            
            for xp in range(0, number_of_buttons):
                # find pivot column
                yp = self.find_pivot(equations, xp, start_y)
                if yp is None:
                    if VERBOSE:
                        print(f"adding free value {xp}")
                    free_values.append(xp)
                    continue
                if VERBOSE:
                    print(f"pivot = {[xp, yp]}")
                pivots.append([xp, yp])
            
                # swap row if needed
                if VERBOSE:
                    print("Checking for row swap")
                if yp != start_y:
                    if VERBOSE:
                        print(f"Swapping {start_y} and {yp}")
                    equations[start_y], equations[yp] = equations[yp], equations[start_y]
                    self.print_equations(equations)
                else:
                    if VERBOSE:
                        print("Row swap not needed")
                yp = start_y
                start_y += 1
            
                # normalise row if needed
                if equations[yp][xp] != 1:
                    factor = equations[yp][xp]
                    if VERBOSE:
                        print(f"Normalising row {yp}")
                    equations[yp] = [a / factor for a in equations[yp]]
                    self.print_equations(equations)
                else:
                    if VERBOSE:
                        print(f"Normalising row {yp} not needed")
            
                # subtract from others rows if 1 in pivot column
                if VERBOSE:
                    print("Subtracting row if needed")
                for y in range(0, joltage_length):
                    if y != yp and equations[y][xp] != 0:
                        if VERBOSE:
                            print(f"Subtracting row {yp} from row {y}")
                        equations[y] = self.normalise(equations[y], equations[yp], equations[y][xp])
                        self.print_equations(equations)
                self.print_equations(equations)
                if VERBOSE:
                    print(pivots)
            
            self.print_equations(equations)
            print(f"pivots: {pivots}")
            print(f"free values: {free_values}")
            if len(free_values) < 3:
                print("Calculating minimum")
                total += self.calculate_minimum(equations, free_values)
            else:
                print(f"Skipping minimum cal: machine{machine_number}")

            # if total == inf:
            #     print(machine_number)
            #     breakpoint()

            print(f"total: {total}")
            print("Next machine\n")
    
    def calculate_minimum(self, equations, free_values):
        max_value = floor(max([equation[-1] * 3 for equation in equations]))
        states = [[]]
        for _ in free_values:
            new_states = []
            for state in states:
                for v in range(0, max_value + 1):
                    new_state = state.copy()
                    new_state.append(v)
                    new_states.append(new_state)
            states = new_states
        print(f"max value: {max_value}")
        if VERBOSE:
            print(f"states: {states}")

        minimum = inf
        for state in states:
            value = self.calculate_value(equations, free_values, state)
            if value < minimum:
                minimum = value
        if VERBOSE:
            print(f"minimum: {minimum}")
        return minimum


    def calculate_value(self, equations, free_values, state):
        total = sum(state)

        for equation in equations:
            total_fv = 0
            for n, fv in enumerate(free_values):
                total_fv += state[n] * equation[fv]

            number_of_presses = equation[-1] - total_fv
            if number_of_presses < 0:
                return inf
            total += number_of_presses
            if VERBOSE:
                print(
                    f"free values {free_values} = {state} for equation {equation} gives number of presses {number_of_presses}")
        if VERBOSE:
            print(f"Total for free values {free_values} = {state} is {total}")
        return total

    def find_pivot(self, equations, column, start_y):
        column = [i for i, row in enumerate(equations[start_y:]) if row[column] != 0]
        if column:
            return column[0] + start_y
            
    def swap_row(self, yp, xp, joltage_length, equations):
        if equations[yp][xp] == 0:
            for y in range(yp + 1, joltage_length):
                if equations[y][xp] == 1:
                    if VERBOSE:
                        print(f"Swapping row {yp} and {y}")
                    equations[y][xp], equations[yp][xp] = equations[yp][xp], equations[y][xp]
                    return

    def normalise(self, row1, row2, factor):
        calculations = zip(row1, row2)
        return [a - b * factor for a, b in calculations]

    def print_equations(self, equations):
        if VERBOSE:
            print(f"Equations: {[[float(a) for a in equation] for equation in equations]}")


    def calculate_equations(self, buttons, joltage):
        arrays = []
        for n in range(0, len(joltage)):
            array = []
            for button in buttons:
                if n in button:
                    array.append(Fraction(1))
                else:
                    array.append(Fraction(0))
            array.append(Fraction(joltage[n]))
            arrays.append(array)
        return arrays
    

start_time = time.time()
# Solve().solve_a('example.txt')
# Solve().solve_a('input_2.txt')
print("\n")
# Solve().solve_b('example.txt')
Solve().solve_b('input.txt')
print("--- %s seconds ---" % (time.time() - start_time))
