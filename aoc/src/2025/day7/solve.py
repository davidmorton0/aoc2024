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
        print(self.width, self.height, self.start_position)

    def solve_a(self, filename):
        input = self.load_input(filename)
        self.set_puzzle_parameters(input)
        self.beams = [[self.start_position]]
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
    
    def calculate_new_beams_b(self, splitters):
        beams = []
        for n, [beam, count] in enumerate(self.beams[-1]):
            if beam in splitters:
                self.merge_beams(n, beams, [beam - 1, count])
                self.merge_beams(n, beams, [beam + 1, count])
            else:
                self.merge_beams(n, beams, [beam, count])
        self.beams.append(beams)
    
    def merge_beams(self, n, beams, beam):
        print(n, beams, beam)
        beam_locations = [b[0] for b in beams] 
        if beam[0] in beam_locations:
            current_beam_location = beam_locations.index(beam[0])
            current_beam, current_count = beams[current_beam_location]
            beams[current_beam_location] = [current_beam, current_count + beam[1]]
        else:
            beams.append([beam[0], beam[1]])
        print(n, beams, beam)
        

    def solve_b(self, filename):
        input = self.load_input(filename)
        self.set_puzzle_parameters(input)
        self.beams = [[[self.start_position, 1]]]
        print(self.beams)
        for line in input[2::2]:
            splitters = self.find_splitters(line)
            self.calculate_new_beams_b(splitters)
            print(self.beams[-1])
        print(self.beam_splits)
        total = sum([b[1] for b in self.beams[-1]])
        print(total)





start_time = time.time()
# Solve().solve_a('example.txt')
# Solve().solve_a('input.txt')
# Solve().solve_a('input_2.txt')
print("\n")
Solve().solve_b('example.txt')
Solve().solve_b('input.txt')
# Solve().solve_b('input_2.txt')
print("--- %s seconds ---" % (time.time() - start_time))