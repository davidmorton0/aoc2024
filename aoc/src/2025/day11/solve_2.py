#!/usr/bin/env python
import time
from copy import deepcopy

import setuptools


class Solve:
    def __init__(self):
        self.connections = {}
        self.current_nodes = {}

    def load_input(self, filename):
        with open(filename, 'r') as file:
            input = file.read().split("\n")
            for line in input:
                key, values = line.split(": ")
                self.connections[key] = values.split(" ")


    def solve(self, filename):
        self.load_input(filename)
        print(self.connections)
        print("\n")
        self.current_nodes["out"] = {"blank": 1, "dac": 0, "fft": 0, "dac_fft": 0}
        
        while node := self.find_next_node():
            self.generate_node(node)
        print(self.current_nodes)

        
    def find_next_node(self):
        current_nodes_keys = self.current_nodes.keys()
        for key in self.connections.keys():
            values = self.connections[key]
            if key not in current_nodes_keys:
                if [value for value in values if value not in current_nodes_keys]:
                    continue
                return key        
        
    
    def generate_node(self, key):
        blank = 0
        dac = 0
        fft = 0
        dac_fft = 0
        for connection in self.connections[key]:
            blank += self.current_nodes[connection]["blank"]
            dac += self.current_nodes[connection]["dac"]
            fft += self.current_nodes[connection]["fft"]
            dac_fft += self.current_nodes[connection]["dac_fft"]
        if key == "dac":
            self.current_nodes[key] = {"blank": 0, "dac": blank + dac, "fft": 0, "dac_fft": fft + dac_fft}
        elif key == "fft":
            self.current_nodes[key] = {"blank": 0, "dac": 0, "fft": blank + fft, "dac_fft": dac + dac_fft}
        else:
            self.current_nodes[key] = {"blank": blank, "dac": dac, "fft": fft, "dac_fft": dac_fft}
        
    



start_time = time.time()
# Solve().solve('example_2.txt')
Solve().solve('input.txt')
print("--- %s seconds ---" % (time.time() - start_time))