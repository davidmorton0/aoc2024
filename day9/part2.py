#!/usr/bin/env python

with open('example.txt', 'r') as file:
    input = file.read().split("\n")[0]

map_contents = [int(digit) for digit in list(input)]
files = {}
spaces = []
file_id = 0
current_block = 'file'
map_position = 0
for digit in map_contents:
    if current_block == 'file':
        files[file_id] = {"length": digit, "start_position": map_position}
        file_id += 1
        current_block = 'space'
    elif current_block == 'space':
        spaces.append({"length": digit, "start_position": map_position})
        current_block = 'file'
    map_position += digit

def find_space(length):
    for n, space in enumerate(spaces):
        if space["length"] >= length:
            return n

def find_end_space(start_position):
    for n, sp in list(enumerate(spaces))[::-1]:
        if sp["start_position"] < start_position:
            return n

def insert_space(length, start_position):
    for o, space in enumerate(spaces):
        if space["start_position"] > start_position:
            spaces.insert(o, {"length": length, "start_position": start_position})
            return

def print_map(files, spaces):
    disk_map = []
    disk_map.extend([{"marker": f"{k}", "length": file["length"], "start_position": file["start_position"]} for k, file in files.items()])
    disk_map.extend(
        [{"marker": ".", "length": space["length"], "start_position": space["start_position"]} for space in spaces])
    disk_map_string = ""
    sorted_disk_map = sorted(disk_map, key=lambda x: x["start_position"])
    for item in sorted_disk_map:
        disk_map_string += item["marker"] * item["length"]
    # print(sorted_disk_map)
    print(disk_map_string)

for m in list(range(0, file_id))[::-1]:
    print_map(files, spaces)
    space = find_space(files[m]["length"])
    if space is not None:
        end_space_position = find_end_space(files[m]["start_position"])
        if end_space_position:
            spaces[end_space_position]["length"] += files[m]["length"]
        else:
            insert_space(files[m]["length"], files[m]["start_position"])
        files[m]["start_position"] = spaces[space]["start_position"]
        spaces[space]["length"] -= files[m]["length"]
        spaces[space]["start_position"] += files[m]["length"]

total = 0
# calculate checksum
for k, file in files.items():
    positions = range(file["start_position"], file["start_position"] + file["length"])
    total += sum([position * k for position in positions])

print(total)
# print(spaces)
print_map(files, spaces)
