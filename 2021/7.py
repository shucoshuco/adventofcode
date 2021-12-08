import os
import functools

def read_input():
    f = open("7.txt", "r")
    ls = [int(x) for x in f.readline().replace("\n", "").split(",")]
    return ls

def median(l):
    size = len(l)
    l.sort()
    return l[int(size / 2)]

def median2(l):
    total = functools.reduce(lambda a, b: a + b, l)
    return int(total / len(l))

def sumatorio(i, value):
    diff = (i - value) if i > value else (value - i)
    result = diff * (diff + 1) / 2
    print("Sumatorio for", i, "/", value, "=", result)
    return result

def calculate(l, value):
    print("List2", l)
    return sumatorio(l[0], value) + functools.reduce(lambda a, b: a + sumatorio(b, value), l) - l[0]

l = read_input()
m = median2(l)
print("List", l)
print("Median", m)

result = None
for i in range(5):
    r1 = calculate(l, m + i)
    print("For", m + i, "=", r1)
    r2 = calculate(l, m - i)
    print("For", m - i, "=", r2)
    if result is None or r1 < result:
        result = r1
    if r2 < result:
        result = r2


print("Result", result)

