#!/usr/bin/env python
import time
from re import split
from itertools import groupby
from collections import defaultdict

start_time = time.time()

INPUT = 1
FILENAME = ['example.txt', 'input_h.txt', 'input_w.txt'][INPUT]

with open(FILENAME, 'r') as file:
    input = [split(r'\s+', line) for line in file.read().split("\n") if line != ""]

def generate_location_ids_list(column, input):
    location_ids = [int(numbers[column]) for numbers in input]
    location_ids.sort()
    return location_ids

def count_location_ids(id_list):
    id_counts = defaultdict(lambda : 0)
    for id, ids in groupby(id_list):
        id_counts[id] = sum(1 for _ in ids)
    return id_counts

def id_differences(ids1, ids2):
    return [abs(id1 - id2) for id1, id2 in zip(ids1, ids2)]

def similarity_scores(ids1, ids2_counts):
    return [ids2_counts[id] * id for id in ids1]

location_ids1 = generate_location_ids_list(0, input)
location_ids2 = generate_location_ids_list(1, input)
location_ids2_counts = count_location_ids(location_ids2)

print(sum(id_differences(location_ids1, location_ids2)))
print(sum(similarity_scores(location_ids1, location_ids2_counts)))
print("--- %s seconds ---" % (time.time() - start_time))