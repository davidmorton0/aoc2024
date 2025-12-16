#!/usr/bin/env python
import time
from itertools import product
from sympy import symbols, Eq, solve
import numpy as np

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
        for machine in self.machines[2:3]:
            joltage = machine["joltage"]
            buttons = machine["buttons"]
            number_of_buttons = len(buttons)
            joltage_length = len(joltage)
            
            equations = self.calculate_equations(buttons, joltage)
            equations.sort(reverse=True)
            print("Calculate equations")
            print(equations)
            pivots = []
            free_values = []
            start_y = 0
            
            for xp in range(0, number_of_buttons):
            # find pivot column
                yp = self.find_pivot(equations, xp, start_y)
                if yp is None:
                    print(f"adding free value {xp}")
                    free_values.append(xp)
                    continue
                print(f"pivot = {[xp, start_y]}")
                pivots.append([xp, start_y])
            
                # swap row if needed
                print("Checking for row swap")
                if yp != start_y:
                    print(f"Swapping {start_y} and {yp}")
                    equations[start_y], equations[yp] = equations[yp], equations[start_y]
                    print(equations)
                else:
                    print("Row swap not needed")
                yp = start_y
                start_y += 1
            
                # invert row if needed
                if equations[yp][xp] == -1:
                    print(f"Inverting row {yp}")
                    equations[yp] = [-a for a in equations[yp]]
                    print(equations)
            
                # subtract from others rows if 1 in pivot column
                print("Subtracting row if needed")
                for y in range(0, joltage_length):
                    if y == yp:
                        continue
                    if equations[y][xp] == 1:
                        print(f"Subtracting row {yp} from row {y}")
                        equations[y] = self.subtract(equations[y], equations[yp])
                        print(equations)
                    elif equations[y][xp] == -1:
                        print(f"Adding row {yp} to row {y}")
                        equations[y] = self.add(equations[y], equations[yp])
                        print(equations)
                print(equations)
                print(pivots)
            
            print(f"equations: {equations}")
            print(f"pivots: {pivots}")
            print(f"free values: {free_values}")    
            
            print("Next machine\n")
    
    def calculate_minimum(self, equations, free_values):
        free_value = 0
        # for equation in equations:
            
    
    def find_pivot(self, equations, column, start_y):
        column = [i for i, row in enumerate(equations[start_y:]) if row[column] != 0]
        # print(f"column {column}")
        if column:
            return column[0] + start_y
            
    def swap_row(self, yp, xp, joltage_length, equations):
        if equations[yp][xp] == 0:
            for y in range(yp + 1, joltage_length):
                if equations[y][xp] == 1:
                    print(f"Swapping row {yp} and {y}")
                    equations[y][xp], equations[yp][xp] = equations[yp][xp], equations[y][xp]
                    return

    def subtract(self, row1, row2):
        calculations = zip(row1, row2)
        return [a - b for a, b in calculations]

    def add(self, row1, row2):
        calculations = zip(row1, row2)
        return [a + b for a, b in calculations]

            # xp, yp = 1, 1
            # 
            # for y in range(yp + 1, joltage_length):
            #     if equations[y][xp + 1] == 1:
            #         print(self.subtract(equations[yp], equations[y]))
            
            # for x in range(xp + 1, joltage_length):
            #     print(equations[x][yp])
            #     if equations[x][yp] == 1:
                    
            
            # for x in range(0, number_of_buttons):
            #     for y in range(x + 1, joltage_length):
            #         print(equations[x][y])
            # for x in range(0, number_of_buttons):
            #     for y in range(x + 1, joltage_length):
            #         print(equations[x][x],equations[y][x]) 
                
            
            # equations[0] = self.subtract(equations[0], equations[1])
            # print(equations)
            # equations[2] = self.subtract(equations[2], equations[3])
            
            
            # A_aug = np.array(equations, dtype=float)
            # A_aug[2] -= 2 * A_aug[0]
            # print("After First Elimination:\n", A_aug)
            # A_aug[2] -= (A_aug[2, 1] / A_aug[1, 1]) * A_aug[1]
            # print("Row Echelon Form:\n", A_aug)
            # count = self.calculate_presses_b(machine)
            # print(count)
            # total += count
        # print(total)
    

            
    
    # def calculate_presses_b(self, machine):        
    #     joltage = machine["joltage"]
    #     buttons = machine["buttons"]
    #     known_values = [[], []]
    #     print(buttons)
    #     print(joltage)
    #     print(known_values)
    #     print("\n")
    #     print(self.check_if_valuse_can_be_calculated(buttons, joltage, known_values))
    #     print(buttons)
    #     print(joltage)
    #     print(known_values)
    #     print("\n")
    #     print(self.check_if_valuse_can_be_calculated(buttons, joltage, known_values))
    #     print("\n")
    #     print("\n")
    #         
    #         
    #     
    # def check_if_valuse_can_be_calculated(self, buttons, joltage, known_values):
    #     buttons_counts = [[] for _ in range(len(joltage))]
    #     for i, button in enumerate(buttons):
    #         if i in known_values[0]:
    #             continue
    #         for connection in button:
    #             buttons_counts[connection].append(i)
    #     for i, button_count in enumerate(buttons_counts):
    #         if len(button_count) == 1:
    #             calculable_buttons = [button_count[0], i]
    #             if calculable_buttons:
    #                 known_values[0].append(calculable_buttons[0])
    #                 known_values[1].append(calculable_buttons[1])
    #                 for value in buttons[calculable_buttons[0]]:
    #                     joltage[value] -= calculable_buttons[1]
    #                 return calculable_buttons
    #     return []
                
        #         return [i, joltage[i]]
        # calculatable_connection = [button_count for button_count in buttons_counts if button_count < 2]
        # if calculatable_connection:
        #     value = calculatable_connection[0]
        #     print(value)
        #     for i, button in enumerate(buttons):
        #         if value in button:
        #             return [value, i]
        # return False
        # for i in range(0, len(joltage)):
        #     if 
        
        # equations = self.calculate_equations(buttons, joltage)
        # print(equations)
        # self.remove_duplicates(equations, joltage)
        # print(equations)
        # print("\n")
        
        
        # A = np.array([[1, 0, 1, 1, 0], [0, 0, 0, 1, 1], [1, 1, 0, 1, 1], [1, 1, 0, 0, 1], [1, 0, 1, 0, 1]])
        # B = np.array([7, 5, 12, 7, 2])
        # B = B.T
        # x = np.linalg.solve(A, B)
        # print(x)
        # A = np.array([[1, 0, 1, 1, 0, 7], [0, 0, 0, 1, 1, 5], [1, 1, 0, 1, 1, 12], [1, 1, 0, 0, 1, 7], [1, 0, 1, 0, 1, 2]])
        # print(np.linalg.solve(A))
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
    
    def calculate_equations(self, buttons, joltage):
        arrays = []
        for n in range(0, len(joltage)):
            array = []
            for button in buttons:
                if n in button:
                    array.append(1)
                else:
                    array.append(0)
            array.append(joltage[n])
            arrays.append(array)
        # arrays.append(joltage)
        return arrays
    
    # def remove_duplicates(self, equations, joltage):
    #     for v, equation in enumerate(equations):
    #         if equation in equations[v+1:]:
    #             i = equations[v+1:].index(equation)
    #             if (joltage[i + v + 1] == joltage[v]):
    #                 print(equations.pop(v), joltage.pop(v))

    # def generate_state_b(self, length, max_value):
    #     states = list(product(range(0, max_value + 1), repeat=length))
    #     for i in range(0, length):
    #         states.append(str(bin(i))[2:].rjust(length, '0'))
    #     return states

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