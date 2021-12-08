import re

val_regex = "([a-z\s]+): ([0-9]+)-([0-9]+) or ([0-9]+)-([0-9]+)"

def read_validations(input):
    validations = {}
    line = input.readline().replace('\n', '')
    while line != '':
        m = re.search(val_regex, line)
        range1 = range(int(m.group(2)), int(m.group(3)) + 1)
        range2 = range(int(m.group(4)), int(m.group(5)) + 1)
        validations[m.group(1)] = list(range1) + list(range2)
        line = input.readline().replace('\n', '')
    return validations

def read_ticket(input):
    line = input.readline()
    if not line:
        return False
    return [int(x) for x in line.replace('\n', '').split(",")]

def validate(ticket, validations):
    for i in ticket:
        valid = False
        for j in validations:
            if i in validations[j]:
                valid = True
        if not valid:
            return i
    return -1

def valid(tickets, validation, i):
    for ticket in tickets:
        if not ticket[i] in validation:
            return False
    return True


def valids(tickets, validations, i, solution):
    solutions = []
    for v in validations:
        if v not in solution and valid(tickets, validations[v], i):
            solutions.append(v)
    return solutions

def find_valids(tickets, validations):
    result = [None] * len(validations)
    for i in range(0, len(validations)):
        result[i] = valids(tickets, validations, i, [])
    return result

def find_next(list, solution):
    value = -1
    min = 100000000000000
    for v in range(0, len(list)):
        if len(list[v]) < min and solution[v] is None:
            value = v
            min = len(list[v])
    return value

def iterate(tickets, list, solution):
    if None not in solution:
        return solution
    i = find_next(list, solution)
    for valid in list[i]:
        if valid not in solution:
            solution[i] = valid
            result = iterate(tickets, list, solution)
            if result:
                return result
            solution[i] = None
    return False

f = open("16-input.txt")
validations = read_validations(f)

f.readline()
own_ticket = read_ticket(f)

f.readline()
f.readline()

ticket = read_ticket(f)
filtered = []

while ticket:
    result = validate(ticket, validations)
    if result < 0:
        filtered.append(ticket)
    ticket = read_ticket(f)

list = find_valids(filtered, validations)


solution = iterate(filtered, list, [None] * len(validations))

prod = 1
for i in range(0, len(solution)):
    if solution[i].startswith('departure'):
        prod = prod * own_ticket[i]

print(prod)
