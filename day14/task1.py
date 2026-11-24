import re

WIDTH = 101
HEIGHT = 103
TIME = 100

def pos_after_100(start: tuple, velocity: tuple) -> tuple:
    return ((start[0] + TIME * velocity[0]) % WIDTH, (start[1] + TIME * velocity[1]) % HEIGHT)

with open("input.txt", 'r') as input:
    tups = []
    PATTERN = r"p=(\d+),(\d+) v=(-?\d+),(-?\d+)"
    for line in input:
        matches = re.findall(PATTERN, line)

        for m in matches:
            tups.append(((int(m[0]), int(m[1])), (int(m[2]), int(m[3]))))

print(tups)
tups_100 = [pos_after_100(tup[0], tup[1]) for tup in tups]
print(tups_100)

quad1: int = 0
quad2: int = 0
quad3: int = 0
quad4: int = 0

for tup in tups_100:
    if tup[0] < WIDTH // 2:
        if tup[1] < HEIGHT // 2:
            quad1 += 1
        elif tup[1] > HEIGHT // 2:
            quad2 += 1
    elif tup[0] > WIDTH // 2:
        if tup[1] < HEIGHT // 2:
            quad3 += 1
        elif tup[1] > HEIGHT // 2:
            quad4 += 1

print(quad1 * quad2 * quad3 * quad4)
