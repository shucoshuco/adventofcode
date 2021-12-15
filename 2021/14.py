import functools

def read_input():
    f = open("14.txt", "r")
    templates = {}
    command = f.readline().replace("\n", "")
    f.readline()
    line = f.readline().replace("\n", "")
    while line != "":
        parts = line.split(" -> ")
        templates[parts[0]] = parts[1]
        line = f.readline().replace("\n", "")

    return command, templates

def count(text):
    values = {}
    for i in text:
        values[i] = functools.reduce(lambda a, b: a + (1 if b == i else 0), text, 0)
    return values

def combine(value1, value2, common = None):
    # print("Value1", value1)
    # print("Value2", value2)
    newvalues = value1.copy()
    for i in value2:
        newvalues[i] = value2[i] + (newvalues[i] if i in newvalues else 0)
    # print("All", newvalues)
    if common is not None:
        newvalues[common] = newvalues[common] - 1
    # print("After fixing", newvalues)
    return newvalues

def resolve(text, size, limit, result, templates):
    if not text in result:
        result[text] = [None] * size 
    if result[text][limit] is not None:
        return
    if limit == 0:
        result[text][0] = count(text)
        return
    part1 = text[0] + templates[text]
    part2 = templates[text] + text[1]
    resolve(part1, size, limit - 1, result, templates)
    resolve(part2, size, limit - 1, result, templates)
    suma = combine(result[part1][limit - 1], result[part2][limit - 1], templates[text])
    result[text][limit] = suma

def print_result(result):
    for i in result:
        print(i, ":", result[i])

def process(text, deep, templates):
    result = {}
    current = {}
    for i in range(len(text) - 1):
        newchar = templates[text[i:i+2]]
        part1 = text[i] + newchar
        part2 = newchar + text[i + 1]
        resolve(part1, deep, deep - 2, result, templates)
        resolve(part2, deep, deep - 2, result, templates)
        suma = combine(result[part1][deep - 2], result[part2][deep - 2], newchar)
        current = combine(current, suma, text[i])
        # print(current)
    # print_result(result)
    return current

def calculate(result):
    maxv = 0
    minv = 100000000000000
    for i in result:
        if result[i] > maxv:
            maxv = result[i]
        if result[i] < minv:
            minv = result[i]
    return maxv - minv

command, tpls = read_input()
#print(command)
#print(tpls)
result = process(command, 41, tpls)
print(result)
print(calculate(result))
