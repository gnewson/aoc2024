def equationValue(equation: list):
    total = int(equation[0][:-1])
    values = equation[1:]
    running_totals = [int(values[0])]
    new_totals = list()

    for value in values[1:]:
        for tot in running_totals:
            new_totals.append(tot + int(value))
            new_totals.append(tot * int(value))
            new_totals.append(int(str(tot) + value))
            #print(new_totals)
        running_totals = new_totals[:]
        new_totals.clear() 

    if total in running_totals:
        return total
    return 0

with open("input.txt", 'r') as input:
    sum_of_equations = 0

    for line in input:
        linelist = line.split()
        sum_of_equations += equationValue(linelist)

print(sum_of_equations)
