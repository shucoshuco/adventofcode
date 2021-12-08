import os
import functools

def read_input():
    f = open("6.txt", "r")
    ls = [int(x) for x in f.readline().replace("\n", "").split(",")]
    return ls

def iterate(l):
    n = l[0]
    for i in range(len(l) - 1):
        l[i] = l[i + 1]
    l[8] = n
    l[6] = l[6] + n
    return l

lanterns = read_input()
print(lanterns)

evolution = [0] * 9
for i in lanterns:
    evolution[i] = evolution[i] + 1

print(evolution)

for i in range(256):
    evolution = iterate(evolution)
    print("Day", i + 1, ":", evolution)

print("Length:", functools.reduce(lambda x, y: x + y, evolution))
