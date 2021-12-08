import copy

def tokenize(line):
    tokens = []
    token = ''
    for i in line:
        if i in ['(', ')', '+', '*', ' ']:
            if token != '':
                tokens.append(int(token))
                token = ''
            if i != ' ':
                tokens.append(i)
        else:
            token = token + i
    if token != '':
        tokens.append(int(token))
    return tokens

def group(tokens):
    grouped = []
    i = 0
    while i < len(tokens):
        if tokens[i] == '(':
            subgroup, processed = group(tokens[i + 1:])
            grouped.append(subgroup)
            i = i + 1 + processed
        elif tokens[i] == ')':
            return grouped, i
        else:
            grouped.append(tokens[i])
        i = i + 1
    return grouped, i

def resolve(list, op, func):
    for i in range(0, len(list)):
        if list[i] == op:
            prefix = list[0:max(0, i - 1)]
            value = func(list[i-1], list[i + 1])
            sufix = list[min(i + 2, len(list)):]
            return resolve(prefix + [value] + sufix, op, func)
    return list

def simplify(group):
    if len(group) == 1:
        return group[0]
    rest = resolve(group, '+', lambda x, y: x + y)
    rest = resolve(rest, '*', lambda x, y: x * y)
    return rest[0]

def process(group):
    for i in range(0, len(group)):
        if isinstance(group[i], list):
            group[i] = process(group[i])
    return simplify(group)

input = open("18-input.txt")
line = input.readline().replace('\n', '')
sum = 0
while line:
    tokens = tokenize(line)
    parts, processed = group(tokens)
    pr = process(parts)
    print(pr)
    sum = sum + pr
    line = input.readline().replace('\n', '')

print(sum)
