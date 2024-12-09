#!/usr/bin/env python

with open('example.txt', 'r') as file:
    input = file.read().split("\n")[0]

map_contents = [int(digit) for digit in list(input)]
map = []
file_id = 0
current_block = 'file'
for digit in map_contents:
    if current_block == 'file':
        map.extend([file_id] * digit)
        file_id += 1
        current_block = 'space'
    elif current_block == 'space':
        map.extend(['.'] * digit)
        current_block = 'file'

while '.' in map:
    last_element = map.pop()
    if last_element != '.':
        map[map.index('.')] = last_element

print(''.join([str(d) for d in map]))

checksum = [d * i for i, d in enumerate(map)]
print(sum(checksum))