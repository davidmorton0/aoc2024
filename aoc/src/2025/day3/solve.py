#!/usr/bin/env python
import time

class Solve:
    def __init__(self):
        self.invalid_ids = []

    def load_input(self, filename):
        with open(filename, 'r') as file:
            input = []
            for line in file.read().split("\n"):
                if line != "":
                    input.append([int(n) for n in list(line)])
            return input


    def solve_a(self, filename):
        input = self.load_input(filename)
        total_joltage = 0
        for battery_bank in input:
            max_value = max(battery_bank)
            index = battery_bank.index(max_value)
            if index > 0:
                first_possibility = max(battery_bank[:index]) * 10 + max_value
            else:
                first_possibility = 0
            if (index + 1) < len(battery_bank):
                second_possibility = max_value * 10 + max(battery_bank[(index + 1):])
            else:
                second_possibility = 0
            print(max_value, index, len(battery_bank), first_possibility, second_possibility)
            total_joltage += max(first_possibility, second_possibility)
        print(input)
        print(total_joltage)



    def solve_b(self, filename):
        input = self.load_input(filename)
        total_joltage = 0
        for battery_bank in input:
            selected_batteries = []
            batteries_for_selection = battery_bank
            for n in range(0, 11):
                print(batteries_for_selection)
                print(batteries_for_selection[0:-11+n])
                selected_battery = max(batteries_for_selection[0:-11 + n])
                selected_batteries.append(selected_battery)
                i = batteries_for_selection.index(selected_battery)
                print("selected:", selected_batteries, "index", i)
                batteries_for_selection = batteries_for_selection[i+1:]
                print(batteries_for_selection)
                print("\n")

            selected_batteries.append(max(batteries_for_selection))
            print(selected_batteries)
            val = int(''.join([str(s) for s in selected_batteries]))
            print(val)
            total_joltage += val
        print(total_joltage)







start_time = time.time()
# Solve().solve_a('example.txt')
# Solve().solve_a('input.txt')
print("\n")
Solve().solve_b('example.txt')
Solve().solve_b('input.txt')
print("--- %s seconds ---" % (time.time() - start_time))