import os
import functools

def read_input():
    f = open("1.txt", "r")
    data = f.readline().replace("\n", "")
    f.close()
    return data

pos = 0
for idx, i in enumerate(read_input()):
    pos = pos + (1 if i == '(' else -1)
    print(pos)
    if pos < 0:
        print("Result:", idx + 1)
        exit(0)

