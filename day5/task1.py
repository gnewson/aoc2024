def middleOrZero(rules: list, pages: list) -> int:
    for rule in rules:
        if rule[0] in pages and rule[1] in pages:
            if pages.index(rule[0]) > pages.index(rule[1]):
                return 0
    return int(pages[len(pages) // 2])


with open("input.txt", 'r') as input:
    blank_line = False
    list_of_pages = []
    rules_list = []

    for line in input:
        if line.isspace():
            blank_line = True
        elif blank_line:
            list_of_pages.append(line.strip().split(","))
        else:
            rules_list.append(line.strip().split("|"))

    sum_of_middles = 0
    for pages in list_of_pages:
        sum_of_middles += middleOrZero(rules_list, pages)

    print(sum_of_middles)
