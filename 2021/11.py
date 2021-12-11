import functools

def read_input():
    f = open("11.txt", "r")
    lines = f.readlines()
    result = []
    for l in lines:
        result.append([int(x) for x in l.replace("\n", "")])
    return result

def adj(x, y, size):
    all = [
            [x - 1, y - 1],
            [x, y - 1],
            [x - 1, y + 1],
            [x - 1, y],
            [x + 1, y],
            [x + 1, y - 1],
            [x, y + 1],
            [x + 1, y + 1]
    ]
    return [x for x in all if x[0] >= 0 and x[0] < size and x[1] >= 0 and x[1] < size]

def inc(table):
    for i in range(len(table)):
        for j in range(len(table[i])):
            table[i][j] = table[i][j] + 1

def flash(table, i, j):
    table[i][j] = 0
    flashes = 1
    for ad in adj(i, j, len(table)):
        x = ad[0]
        y = ad[1]
        if table[x][y] > 0:
            table[x][y] = table[x][y] + 1
            if table[x][y] >= 10:
                flashes = flashes + flash(table, x, y)
    return flashes

def count_zeros(table):
    suma = 0
    for i in range(len(table)):
        for j in range(len(table[i])):
            if table[i][j] == 0:
                suma = suma + 1
    return suma

def iterate(table):
    flashes = 0
    for i in range(len(table)):
        for j in range(len(table[i])):
            if table[i][j] == 10:
                flashes = flashes + flash(table, i, j)
    return flashes >= len(table) * len(table), flashes

table = read_input()
total = 0
i = 0
completed, flashes = iterate(table)
while not completed and i < 1000:
    i = i + 1
    inc(table)
    print("Flashes in ", i, ":", flashes)
    completed, flashes = iterate(table)
print("Result:", i)

