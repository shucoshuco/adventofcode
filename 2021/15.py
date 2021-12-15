import sys
import functools

def read_input():
    f = open("15.txt", "r")
    square = []
    line = f.readline().replace("\n", "")
    while len(line) > 0:
        square.append([int(i) for i in line])
        line = f.readline().replace("\n", "")
    f.close()
    return square

def next_value(i):
    return 1 if i + 1 > 9 else i + 1

def print_matrix(matrix):
    print("------------------------------------")
    for i in matrix:
        print(functools.reduce(lambda a, b: "{}  {}".format(a, b), i))

def expand(square):
    height = len(square)
    width = len(square[0])
    for row in square:
        for i in range(4):
            row.extend([None] * width)
            for j in range(width):
                row[(i + 1) * height  + j] = next_value(row[i * height + j])
    for i in range(4):
        for j in range(height):
            y = (i + 1) * height + j
            square.extend([[None] * 5 * width])
            for x in range(len(square[y])):
                square[y][x] = next_value(square[i * height + j][x])

    return square

def set(square, solution, y, x, current):
    calc = current + square[y][x]
    if solution[y][x] is None or solution[y][x] > calc:
        solution[y][x] = calc
        return True
    return False

def adjs(y, x, height, width):
    offset = [
            [1, 0],
            [0, 1],
            [0, -1],
            [-1, 0],
    ]
    adjs = []
    for i in offset:
        y1 = y + i[0]
        x1 = x + i[1]
        if y1 >= 0 and y1 < height and x1 >= 0 and x1 < width:
            adjs.append([y1, x1])
    return adjs

def min_adjs(solutions, y, x, height, width):
    point = None
    mini = 100000000000
    for adj in adjs(y, x, height, width):
        value = solutions[adj[0]][adj[1]]
        if value is not None:
            mini = min(mini, value)
    return mini

def resolve(square):
    solution = [None] * len(square)
    for i in range(len(solution)):
        solution[i] = [None] * len(square[0])
    sol = 0
    solution[0][0] = 0
    it = 1
    while sol != solution[-1][-1]:
        print("Iteration", it)
        sol = solution[-1][-1]
        for i in range(len(square)):
            for j in range(len(square[i])):
                if i > 0 or j > 0:
                    solution[i][j] = min_adjs(solution, i, j, len(square), len(square[i])) + square[i][j]
        it = it + 1
    return sol

square = read_input()
square = expand(square)
sol = resolve(square)
print("Solution:", sol)
