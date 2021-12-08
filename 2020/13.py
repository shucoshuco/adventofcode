import math
from functools import reduce

def parse_input(line):
    result = [[1, 0]]
    for i in range(0, len(line)):
        if line[i] != 'x':
            result.append([int(line[i]), i])
    return result

def next_match(ref, next, i, step):
    while True:
        if (ref * i + next[1]) % next[0] == 0:
            return i
        i = i + step

def process(buses):
    print(buses)
    ref = buses[0][0]
    step = 1

    for i in range(1, len(buses)):
        ref = next_match(buses[0][0], buses[i], ref, step)
        step = step * buses[i][0]
        print(ref)

f = open("13-input.txt")
f.readline()
line = f.readline()
while line:
    buses = parse_input(line.replace('\n', '').split(','))
    process(buses)
    line = f.readline()

