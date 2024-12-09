def correctDifferences(report: list):
    for i in range(1, len(report)):
        val = abs(int(report[i]) - int(report[i-1]))
        if val not in [1, 2, 3]:
            return False
    return True

def reportIncreasing(report: list):
    for i in range(1, len(report)):
        if int(report[i]) <  int(report[i-1]):
            return False
    return True

def reportDecreasing(report: list):
    for i in range(1, len(report)):
        if int(report[i]) >  int(report[i-1]):
            return False
    return True

def isSafe(report: str):
    if (correctDifferences(report) and
        (reportIncreasing(report) or reportDecreasing(report))):
        return True
    for i in range(0, len(report)):
        if (correctDifferences(report[:i] + report[(i + 1):]) and
            (reportIncreasing(report[:i] + report[(i + 1):]) or
             reportDecreasing(report[:i] + report[(i + 1):]))):
            return True
    return False


safe_count = 0

with open("input.txt", 'r') as input:
    for line in input:
        if isSafe(line.split()):
            safe_count += 1

print(f"Safe count is {safe_count}")
