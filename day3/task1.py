import re

with open("input.txt", 'r') as input:
    pattern = "mul\((\d+),(\d+)\)"
    total = 0
    for line in input:
        pairs = re.findall(pattern, line)

        for pair in pairs:
            total += int(pair[0]) * int(pair[1])


print(total)

