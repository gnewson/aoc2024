import re

WIDTH = 101
HEIGHT = 103

def pos_after_iter(start: tuple, velocity: tuple, iteration: int) -> tuple:
    return ((start[0] + iteration * velocity[0]) % WIDTH, (start[1] + iteration * velocity[1]) % HEIGHT)

with open("input.txt", 'r') as input:
    tups = []
    PATTERN = r"p=(\d+),(\d+) v=(-?\d+),(-?\d+)"
    for line in input:
        matches = re.findall(PATTERN, line)

        for m in matches:
            tups.append(((int(m[0]), int(m[1])), (int(m[2]), int(m[3]))))

found = False
duplicates = False
iteration = 0
while(not found):
    iteration += 1;
    next_tups = [pos_after_iter(tup[0], tup[1], iteration) for tup in tups]
    for list_tup in next_tups:
        if next_tups.count(list_tup) > 1:
            duplicates = True
            break
    if not duplicates:
        found = True
    else:
        duplicates = False
print(iteration)

