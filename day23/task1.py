def prune(sn: int) -> int:
    return sn % 16777216

def mix(sn: int, value: int) -> int:
    return sn ^ value

def next_secret_number(number: int):
    stage1 = prune(mix(number, number * 64))
    stage2 = prune(mix(stage1, stage1 // 32))
    return prune(mix(stage2, stage2 * 2048))

starters = []
enders = []

with open("input.txt", 'r') as input:

    for line in input:
        starters.append(int(line.strip()))

for start in starters:
    count = 0
    while(count < 2000):
        start = next_secret_number(start)
        count += 1
    enders.append(start)

total = 0
for end in enders:
    total += end

print(total)
