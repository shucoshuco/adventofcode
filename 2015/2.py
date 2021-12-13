import os
import functools

def read_input():
    f = open("2.txt", "r")
    data = []
    for d in f.readlines():
        data.append([int(x) for x in d.replace("\n", "").split("x")])
    f.close()
    return data

def calculate_sides(dims):
    return [
            dims[0] * dims[1],
            dims[0] * dims[2],
            dims[2] * dims[1],
    ]

def calculate_paper(dims):
    sides = calculate_sides(dims)
    sides.sort()
    return functools.reduce(lambda a, b: a + 2 * b, sides, 0) + sides[0]

def calculate_ribbon(dims):
    dims.sort()
    return 2 * dims[0] + 2 * dims[1] + dims[0]*dims[1]*dims[2]

paper = 0
ribbon = 0
for input in read_input():
    paper = paper + calculate_paper(input)
    ribbon = ribbon + calculate_ribbon(input)

print("Paper:", paper)
print("Ribbon:", ribbon)
