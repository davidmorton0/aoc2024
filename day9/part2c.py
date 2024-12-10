#!/usr/bin/env python

with open('input.txt', 'r') as file:
    input = file.read().split("\n")[0]

map_contents = [int(digit) for digit in list(input)]
file_id = 0
current_block = 'file'
disk_map = []
for digit in map_contents:
    if current_block == 'file':
        disk_map.extend([file_id] * digit)
        file_id += 1
        current_block = 'space'
    elif current_block == 'space':
        disk_map.extend(['.'] * digit)
        current_block = 'file'
max_file_id = file_id - 1
print(f"max file id: {max_file_id}")

for file_id in list(range(0, max_file_id + 1))[::-1]:
    print(f"file id: {file_id}")
    # print(''.join([str(x) for x in disk_map]))
    file_locations = [[file_id, index] for index, location in enumerate(disk_map) if location == file_id]
    file_length = len(file_locations)
    start_location = file_locations[0][1]
    end_location = file_locations[-1][1]

    space = False
    spaces = []
    for index, location in enumerate(disk_map):
        if not space and location == '.':
            space = True
            current_space_index = index
            current_space_length = 1
        elif space and location == '.':
            current_space_length += 1
        elif space and location != '.':
            spaces.append([current_space_index, current_space_length])
            space = False
    for start_index, length in spaces:
        if length >= file_length and start_index < start_location:
            for i in range(start_location, end_location + 1):
                disk_map[i] = '.'
            for i in range(start_index, start_index + file_length):
                disk_map[i] = file_id
            break
print(sum([i * f_id for i, f_id in enumerate(disk_map) if f_id != '.']))