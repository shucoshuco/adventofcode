import os
import functools
from enum import Enum

def read_input():
    f = open("8-ex.txt", "r")
    line = f.readline().replace("\n", "")
    nos = []
    while len(line) > 0:
        parts = line.split(" | ")
        nos.append([parts[0].split(" "), parts[1].split(" ")])
        line = f.readline().replace("\n", "")
    return nos

class Position(Enum):
    UP = 1
    LUP = 2
    RUP = 3
    MID = 4
    LDOWN = 5
    RDOWN = 6
    DOWN = 7

class Digit:
    positions = {}
    found = {}

    def __init__(self):
        for p in Position:
            self.positions[p] = ['a', 'b', 'c', 'd', 'e', 'f', 'g']

    def get_positions(self, value):
        if value == 2:
            return [Position.RUP, Position.RDOWN]
        if value == 3:
            return [Position.UP, Position.RUP, Position.RDOWN]
        if value == 4:
            return [Position.LUP, Position.MID, Position.RUP, Position.RDOWN]
        if value == 5: return list(Position)
        if value == 6: return list(Position)
        if value == 7: return list(Position)

    def apply(self, chain):
        validPos = self.get_positions(len(chain))
        for p in Position:
            if p in validPos:
                self.positions[p] = [x for x in self.positions[p] if x in chain]
            else:
                self.positions[p] = [x for x in self.positions[p] if x not in chain]
        print("After checking", chain)
        print("validPos", validPos)
        print(self.positions)
        for c in chain:
            pos = None
            options = 0
            for p in validPos:
                if c in self.positions[p]:
                    pos = p
                    options = options + 1
            if options == 1:
                self.found[pos] = c

    def print(self):
        print(self.found)

def found(l):
    l.sort(key=lambda x: len(x))
    print(l)
    d = Digit()
    for digit in l:
        d.apply(digit)
    d.print()

input = read_input()
for l in input:
    found(l[0])
    exit(1)

