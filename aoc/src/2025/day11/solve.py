#!/usr/bin/env python
import time
from copy import deepcopy

import setuptools


class Solve:
    def __init__(self):
        self.connections = {}
        self.finished_paths = []

    def load_input(self, filename):
        with open(filename, 'r') as file:
            input = file.read().split("\n")
            for line in input:
                key, values = line.split(": ")
                self.connections[key] = values.split(" ")


    def solve_a(self, filename):
        self.load_input(filename)
        print(self.connections)
        paths = [["svr"]]
        
        while paths:
            print(paths)
            paths = self.find_new_paths(paths)
        
        print(self.finished_paths)
        print(paths)
        print(len(self.finished_paths))
    
    def find_new_paths(self, paths):
        next_paths = []
        for path in paths:
            new_paths = self.find_next_connections(path)
            for new_path in new_paths:
                if new_path[-1] == "tty":
                    self.finished_paths.append(new_path)
                elif new_path[-1] == "out":
                    pass
                else:
                    next_paths.append(new_path)
        return next_paths
        
    
    def find_next_connections(self, path):
        new_connections = self.connections[path[-1]]
        new_paths = []
        for new_connection in new_connections:
            # print(path)
            if new_connection in path:
                continue
            new_path = deepcopy(path)
            new_path.append(new_connection)
            new_paths.append(new_path)
        return new_paths

    def solve_b(self, filename):
        self.load_input(filename)
        print(self.connections)
        path_sizes = self.generate_path_sizes()
        # paths = { "svr": 1 }
        # self.finished_paths = {}
        # 
        # while paths:
        #     print(paths)
        #     paths = self.find_new_paths_2(paths)
        # 
        # print(self.finished_paths)
        # 
        # correct_paths = [path for path in self.finished_paths if "dac" in path and "fft" in path]
        # print("\n")
        # print(len(self.finished_paths))
        # print(len(correct_paths))
    
    def find_new_paths_2(self, paths):
        next_paths = {}
        
        for path_key in paths.keys():
            self.find_next_connections_2(path_key, paths, next_paths)
        return next_paths
    
    def generate_path_sizes(self):
        path_sizes = {"svr": 1}
        path_sizes_length = 0
        while len(path_sizes) != path_sizes_length:
            path_sizes_length = len(path_sizes)
            self.check_connections(path_sizes)
            print(path_sizes)
            print(path_sizes_length)        
        return path_sizes
        # for key in connections.keys():
        #     absent_keys = [connection for connection in connections[key] if connection not in path_sizes.keys()]
        #     if not absent_keys:
        #         total = 0
        #         for connection in connections[key]:
        #             total += path_sizes[connection]
        #         path_sizes[key] = total

    
    def check_connections(self, path_sizes):
        path_sizes_keys = path_sizes.keys()
        for key in self.connections.keys():
            if self.check_connection(self.connections[key], path_sizes_keys):
                path_sizes[key] = self.calculate_connection(key, path_sizes)
    
    def check_connection(self, connection, path_sizes_keys):
        for value in connection:
            if value not in path_sizes_keys:
                return False
        return True
    
    def calculate_connection(self, key, path_sizes):
        total = 0
        for connection in self.connections[key]:
            total += path_sizes[connection]
        return total

            
    def find_next_connections_2(self, path_key, paths, next_paths):
        last_connection = path_key.split(",")[-1]
        new_connections = self.connections[last_connection]
        for new_connection in new_connections[-1:]:
            new_key = path_key + "," + new_connection
            if new_connection == "out":
                if self.finished_paths.get(new_key):
                    self.finished_paths[new_key] += paths[path_key]
                else:
                    self.finished_paths[new_key] = paths[path_key]
            elif next_paths.get(new_key):
                next_paths[new_key] += paths[path_key]
            else:
                next_paths[new_key] = paths[path_key]



start_time = time.time()
# Solve().solve_a('example.txt')
# Solve().solve_a('input.txt')
print("\n")
# Solve().solve_b('example_2.txt')
Solve().solve_b('input.txt')
print("--- %s seconds ---" % (time.time() - start_time))