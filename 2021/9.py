import functools

def read_input():
    f = open("9.txt", "r")
    line = f.readline().replace("\n", "")
    mapa = []
    while len(line) > 0:
        mapa.append(line)
        line = f.readline().replace("\n", "")
    return mapa

def into_limit(mapa, x, y):
    return x >= 0 and y >= 0 and x < len(mapa) and y < len(mapa[0])

def check(mapa, x, y, x1, y1):
    if not into_limit(mapa, x1, y1):
        return True
    return int(mapa[x][y]) < int(mapa[x1][y1])

def adj(x, y):
    return [[x, y - 1], [x - 1, y], [x + 1, y], [x, y + 1]]

def valid(mapa, x, y):
    return functools.reduce(lambda a, b: a and check(mapa, x, y, b[0], b[1]), adj(x, y), True)

def calculate_basist(mapa, ref, x, y, current):
    if into_limit(mapa, x, y) and int(mapa[x][y]) < 9 and int(mapa[x][y]) > int(ref):
        current[str(x) + str(y)] = True
        for i in adj(x, y):
            calculate_basist(mapa, mapa[x][y], i[0], i[1], current)
    return len(current)

def find(mapa):
    values = []
    size = len(mapa)
    for j in range(len(mapa)):
        for i in range(len(mapa[j])):
            if valid(mapa, j, i):
                size = calculate_basist(mapa, "-1", j, i, {})
                values.append(size)
    return values

mapa = read_input()
values = find(mapa)
values.sort(reverse = True)
print("Result:", functools.reduce(lambda a, b: a * b, values[0:3]))

