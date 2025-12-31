#!/usr/bin/env python
import time

class Solve:
    def __init__(self):
        self.shapes = []
        self.spaces = []
        self.full_spaces = []

    def load_input(self, filename):
        with open(filename, 'r') as file:
            input = file.read().split("\n")
            for n in range(0,6):
                self.load_piece(input[n * 5 + 1: n * 5 + 4])
            # print(self.shapes)
            space_strings = input[30:]
            for space_string in space_strings:
                self.load_space(space_string)
            # print(self.spaces)
    
    def load_space(self, space_string):
        size, piece_string = space_string.split(": ")
        width, height = size.split("x")
        pieces = [int(piece) for piece in piece_string.split(" ")]
        self.spaces.append({
            "width": int(width),
            "height": int(height),
            "pieces": pieces,
            "fits": None
        })
    
    def load_piece(self, piece_strings):
        self.shapes.append({
            "rows": piece_strings,
            "size": len([c for c in ''.join(piece_strings) if c == "#"])
        })


    def solve(self, filename):
        self.load_input(filename)
        print(self.count_undecided_spaces())
        for space in self.spaces:
            self.check_size(space)
        print(self.count_undecided_spaces())
    
    def count_undecided_spaces(self):
        return len([space for space in self.spaces if space["fits"] is None])
    
    def check_size(self, space):
        width, height, pieces, fits = space.values()
        total_piece_size = 0
        for n, piece in enumerate(pieces):
            total_piece_size += self.shapes[n]["size"] * piece
        allowed_gaps = width * height - total_piece_size
        space["allowed_gaps"] = allowed_gaps
        print(width * height, total_piece_size, allowed_gaps)
        if allowed_gaps < 0:
            space["fits"] = False
        # elif allowed_gaps < 20:
        #     print(space)
    
    # def calculate_complete_rectangles(self):
    #     for n, start_shape in enumerate(self.shapes):
    #         row = [n]
    #         last_shape = ['#', '#', '#']
    #         first_shape = start_shape
    #         print(last_shape)
    #         print(start_shape)
    #         fit = self.calculate_fit(last_shape, first_shape)
    #         if fit[0]:
    #             self.full_spaces.append(row)
    #         print("\n")
    #         print(self.full_spaces)
    #         # for m, shape in enumerate(self.shapes()):
    #         #     fit = self.calculate_fit(last_shape, first_shape)
    #         #     if fit[0]:
    #         #         self.full_spaces.append([n, m])
    #         #         
    #         
    # 
    # def calculate_fit(self, last_shape, new_shape):
    #     last_shape_ends = [row[::-1].index("#") for row in last_shape]
    #     new_shape_ends = [row.index("#") for row in new_shape]
    #     fit = []
    #     for n in range(0, 3):
    #         fit.append(last_shape_ends[n] - new_shape_ends[n])
    #     print(last_shape_ends)
    #     print(new_shape_ends)
    #     print(fit)
    #     if fit[0] == fit[1] and fit[1] == fit[2]:
    #         
    #         return [True, 0]
    #     else:
    #         return [False]
    
    # def is_end(self):
        
        
        





start_time = time.time()
Solve().solve('example.txt')
Solve().solve('input.txt')
print("--- %s seconds ---" % (time.time() - start_time))