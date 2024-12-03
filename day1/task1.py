import functools

list1 = list() 
list2 = list() 

def tupDiff(tup):
    return abs(int(tup[0]) - int(tup[1]))

with open("input.txt", 'r') as input:
  for line in input:
    linepair = line.split()
    first = linepair[0]
    second = linepair[1]

    list1.append(first)
    list2.append(second)


list1.sort()
list2.sort()

list_zip = zip(list1, list2)
zipped_list = list(list_zip)

mapped_list = map(tupDiff, zipped_list)
list_sum = functools.reduce(lambda x, y: x + y, mapped_list)

print(list_sum)
