def possible(pattern: str, towels: list) -> bool:
    remaining_pattern = pattern
    possible = True

    while(len(remaining_pattern) > 0):
        print(remaining_pattern)
        found = False
        for towel in towels:
            if remaining_pattern.startswith(towel):
                print(towel)
                remaining_pattern = remaining_pattern[len(towel):]
                found = True
                break
        if not found:
            possible = False
            break
    print(possible)
    return possible

with open("input.txt", 'r') as input:
    blank_line = False
    desired = []
    available = []

    for line in input:
        if line.isspace():
            blank_line = True
        elif blank_line:
            desired.append(line.strip())
        else:
            available = line.strip().split(", ")

available.sort(key=len, reverse=False)
count = 0
for pattern in desired:
    if possible(pattern, available):
        count += 1
print(count)
