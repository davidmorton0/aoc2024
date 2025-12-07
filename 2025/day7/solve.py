#!/usr/bin/env python
import time

class Solve:
    def __init__(self):
        self.values = []
        self.beam_splits = 0

    def load_input(self, filename):
        with open(filename, 'r') as file:
            input = file.read().split("\n")
            return input
    
    def set_puzzle_parameters(self, input):
        self.width = len(input[0])
        self.height = len(input)
        self.start_position = input[0].index("S")
        self.beams = [[self.start_position]]
        print(self.width, self.height, self.start_position, self.beams)

    def solve_a(self, filename):
        input = self.load_input(filename)
        self.set_puzzle_parameters(input)
        for line in input[2::2]:
            splitters = self.find_splitters(line)
            self.calculate_new_beams(splitters)
            print(self.beam_splits)
        print(self.beams)
        print(self.beam_splits)
    
    def find_splitters(self, row):
        splitters = []
        for n, space in enumerate(row):
            if space == "^":
                splitters.append(n) 
        return splitters
    
    def calculate_new_beams(self, splitters):
        beams = []
        for beam in self.beams[-1]:
            if beam in splitters:
                self.beam_splits += 1
                if beam - 1 not in beams:
                    beams.append(beam - 1)
                if beam + 1 not in beams:
                    beams.append(beam + 1)
            else:
                if beam not in beams:
                    beams.append(beam)
        self.beams.append(beams)

    def solve_b(self, filename):
        input = self.load_input(filename)





start_time = time.time()
Solve().solve_a('example.txt')
# Solve().solve_a('input.txt')
Solve().solve_a('input_2.txt')
print("\n")
# Solve().solve_b('example.txt')
# Solve().solve_b('input.txt')
# Solve().solve_b('input_2.txt')
print("--- %s seconds ---" % (time.time() - start_time))