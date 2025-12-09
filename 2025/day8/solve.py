#!/usr/bin/env python
import math
import time

class Solve:
    def __init__(self):
        self.values = []

    def load_input(self, filename):
        with open(filename, 'r') as file:
            input = file.read().split("\n")
            coordinates = [[int(number) for number in line.split(",")] for line in input]
                
            return coordinates


    def solve_a(self, filename):
        coordinates = self.load_input(filename)
        lowest = []
        for m, coordinate_1 in enumerate(coordinates):
            for n, coordinate_2 in enumerate(coordinates):
                if m >= n:
                    continue
                distance = self.find_distance(coordinate_1, coordinate_2)
                if not lowest or distance < lowest[-1][0]:
                    lowest.append([distance, coordinate_1, coordinate_2, m, n])
                    lowest = sorted(lowest, key=lambda x : x[0])[:1000]
        print(lowest)
        
        circuits = self.calculate_circuits(lowest, len(coordinates))
        print(circuits)
        circuit_lengths = [len(circuit) for circuit in circuits]
        circuit_lengths.sort()
        print(circuit_lengths)
        print(circuit_lengths[-3:])
        print(circuit_lengths[-3] * circuit_lengths[-2] * circuit_lengths[-1])

            
        # print(coordinates)
        # print(self.find_distance(coordinates[0], coordinates[1]))
    
    def find_distance(self, coordinate_1, coordinate_2):
        x1, y1, z1 = coordinate_1
        x2, y2, z2 = coordinate_2
        flat_distance_sq = ((x1 - x2) ** 2) + (y1 - y2) ** 2
        distance = math.sqrt(flat_distance_sq + (z1 - z2) ** 2)
        return distance
    
    def calculate_circuits(self, lowest, number_of_coordinates):
        circuits = []
        for n in list(range(0, number_of_coordinates)):
            circuits.append([n])
        for junction_box in lowest:
            # print(circuits)
            jb1 = junction_box[3]
            jb2 = junction_box[4]
            for n, circuit in enumerate(circuits):
                if jb1 in circuit:
                    circuit1 = n
                if jb2 in circuit:
                    circuit2 = n
            if circuit1 != circuit2:
                # print(circuit1, circuit2)
                combined_circuit = circuits[circuit1] + circuits[circuit2]
                circuits[circuit1] = combined_circuit
                circuits.pop(circuit2)
        return circuits
            
                
                
        

    def solve_b(self, filename):
        coordinates = self.load_input(filename)
        lowest = []
        for m, coordinate_1 in enumerate(coordinates):
            for n, coordinate_2 in enumerate(coordinates):
                if m >= n:
                    continue
                distance = self.find_distance(coordinate_1, coordinate_2)
                if not lowest or distance < lowest[-1][0]:
                    lowest.append([distance, coordinate_1, coordinate_2, m, n])
                    lowest = sorted(lowest, key=lambda x: x[0])[:4941]
        print(lowest)

        circuits = self.calculate_circuits(lowest, len(coordinates))
        # print(circuits)
        circuit_lengths = [len(circuit) for circuit in circuits]
        circuit_lengths.sort()
        # print(circuits)
        print(circuit_lengths[-3:])
        last_connection = lowest[-1]
        c1 = last_connection[1]
        c2 = last_connection[2]
        print(c1[0] * c2[0])
        # print(coordinates[circuits[-2][0]][0] * coordinates[circuits[-1][0]][0])





start_time = time.time()
# Solve().solve_a('example.txt')
# Solve().solve_a('input.txt')
print("\n")
# Solve().solve_b('example.txt')
Solve().solve_b('input.txt')
print("--- %s seconds ---" % (time.time() - start_time))