#!/usr/bin/env python
import time
from itertools import product
from sympy import symbols, Eq, solve
DIGITS = "abcdefghijklmn"

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
        total = 0
        for machine in self.machines:
            count = self.calculate_presses_b(machine)
            # print(count)
            # total += count
        print(total)
    
    def calculate_presses_b(self, machine):        
        joltage = machine["joltage"]
        buttons = machine["buttons"]
        a, b, c, d, e, f = symbols("a b c d e f", integer=True)
        eq1 = Eq(d + f, 3)
        eq2 = Eq(b + f, 5)
        eq3 = Eq(c + d + e, 4)
        eq4 = Eq(a + b + d, 7)
        solution = solve([eq1,eq2, eq3, eq4], (a,b,c,d,e,f))
        print(solution)
        
        # states = self.generate_state_b(len(buttons), max(joltage))
        # lowest = None
        # for state in states:
        #     print(state)
        #     # for button in buttons:
        #     #     if state[n] == "1":
        #     #         lights_state = self.press_button(buttons[n], lights_state)
        #     # if lights_state == joltage:
        #     #     button_presses = sum([int(i) for i in list(state)])
        #     #     if lowest is None or button_presses < lowest:
        #     #         lowest = button_presses
        # return lowest

    def generate_state_b(self, length, max_value):
        states = list(product(range(0, max_value + 1), repeat=length))
        for i in range(0, length):
            states.append(str(bin(i))[2:].rjust(length, '0'))
        return states

start_time = time.time()
# Solve().solve_a('example.txt')
# Solve().solve_a('input_2.txt')
print("\n")
Solve().solve_b('example.txt')
# Solve().solve_b('input.txt')
print("--- %s seconds ---" % (time.time() - start_time))

# from sympy import symbols, Eq, solve

# from sympy import symbols, Eq, solve
# 
# # Define symbolic variables
# a, b = symbols('a b', integer=True)
# 
# # Define the equations
# eq1 = Eq(a * 51 + b * 21, 6177)
# eq2 = Eq(a * 17 + b * 65, 5597)
# 
# # Solve the system of equations
# solution = solve([eq1, eq2], (a, b))
# 
# # Output the solution
# print("Solution:", solution)