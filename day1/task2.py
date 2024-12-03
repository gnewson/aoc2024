import functools

list1 = list() 
list2 = list() 
total = 0

def tupDiff(tup):
    return abs(int(tup[0]) - int(tup[1]))

with open("input.txt", 'r') as input:
  for line in input:
    linepair = line.split()
    first = linepair[0]
    second = linepair[1]

    list1.append(first)
    list2.append(second)

for item in list1:
  total += int(item) * list2.count(item)

print(total)
