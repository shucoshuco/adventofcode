import sys
import functools
import math
import time

class Number:
    def __init__(self):
        self.foo = 0

class LiteralNumber(Number):

    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

    def accept(self, value, left):
        self.value = self.value + value.value
        return None

    def can_explode(self):
        return False, None, None

    def explode(self, level = 0):
        return False, None, None

    def split(self):
        if self.value >= 10:
            left = LiteralNumber(math.floor(self.value / 2))
            right = LiteralNumber(math.ceil(self.value / 2))
            return True, ComplexNumber(left, right)
        return False, self

    def magnitude(self):
        return self.value

    def copy(self):
        return LiteralNumber(self.value)

class ComplexNumber(Number):

    def __init__(self, left, right):
        self.left = left
        self.right = right

    def __str__(self):
        return "[{},{}]".format(self.left, self.right)

    def accept(self, value, left):
        return self.left.accept(value, left) if left else self.right.accept(value, left)

    def can_explode(self):
        return True, self.left, self.right

    def explode(self, level = 0):
        if level == 3:
            explode, left, right = self.left.can_explode()
            if explode:
                right = self.right.accept(right, True)
                self.left = LiteralNumber(0)
            if not explode:
                explode, left, right = self.right.can_explode()
                if explode:
                    left = self.left.accept(left, False)
                    self.right = LiteralNumber(0)
            return explode, left, right
        explode, left, right = self.left.explode(level + 1)
        if explode and right is not None:
            right = self.right.accept(right, True)
        if not explode:
            explode, left, right = self.right.explode(level + 1)
            if explode and left is not None:
                left = self.left.accept(left, False)
        return explode, left, right

    def split(self):
        splitted, self.left = self.left.split()
        if not splitted:
            splitted, self.right = self.right.split()
        return splitted, self

    def reduce(self):
        pending = True
        while pending:
            exploded, left, right = self.explode()
            splitted = False
            if not exploded:
                splitted, foo = self.split()
            pending = exploded or splitted
        return self

    def magnitude(self):
        return self.left.magnitude() * 3 + self.right.magnitude() * 2

    def copy(self):
        return ComplexNumber(self.left.copy(), self.right.copy())

def read_literal(line, start):
    idx = start
    while line[idx + 1].isnumeric():
        idx = idx + 1
    return LiteralNumber(int(line[start:idx + 1])), idx

def read_number(line, start):
    internals = []
    idx = start
    sep = start
    while idx < len(line):
        if line[idx] == '[':
            number, idx = read_number(line, idx + 1)
            internals.append(number)
        elif line[idx] == ',':
            sep = idx + 1
        elif line[idx] == ']':
            number = ComplexNumber(internals[0], internals[1])
            return number, idx
        else:
            number, idx = read_literal(line, idx)
            internals.append(number)
        idx = idx + 1
    raise "Wrong number!!"

def read_input():
    f = open("18.txt", "r")
    numbers = [read_number(i.replace("\n", ""), 1) for i in f.readlines()]
    f.close()
    return [i[0] for i in numbers]


def add_numbers(n1, n2):
    return ComplexNumber(n1, n2).reduce()

numbers = read_input()
total = numbers[0]

#for i in range(len(numbers) - 1):
    #print(" ", total)
    #print("+", numbers[i + 1])
    #total = add_numbers(total, numbers[i + 1])
    #print("=", total)
    #print()

maxim = 0
for i in range(len(numbers) - 1):
    for j in range(len(numbers) - i - 1):
        copy1 = numbers[i].copy()
        copy2 = numbers[i + j + 1].copy()
        maxim = max(maxim, add_numbers(copy1, copy2).reduce().magnitude())
        copy1 = numbers[i + j + 1].copy()
        copy2 = numbers[i].copy()
        maxim = max(maxim, add_numbers(copy1, copy2).reduce().magnitude())

print("Result:", maxim)


