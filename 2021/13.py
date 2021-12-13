import functools

def build_matrix(points):
    xsize = functools.reduce(lambda a, b: max(a, b[0]), points, 0) + 1
    ysize = functools.reduce(lambda a, b: max(a, b[1]), points, 0) + 1
    matrix = []
    for i in range(ysize):
        matrix.append([False] * xsize)
    for i in points:
        matrix[i[1]][i[0]] = True
    return matrix

def read_input():
    f = open("13.txt", "r")
    points = []
    line = f.readline().replace("\n", "")
    while line != "":
        points.append([int(x) for x in line.split(",")])
        line = f.readline().replace("\n", "")

    instructions = []
    line = f.readline().replace("\n", "")
    while len(line) > 0:
        parts = line.split(" ")
        inst = parts[2].split("=")
        instructions.append([inst[0], int(inst[1])])
        line = f.readline().replace("\n", "")

    return build_matrix(points), instructions

def print_line(line):
    txt = functools.reduce(lambda a, b: a + ('#' if b else '.'), line, "")
    print(txt)

def print_v_line(line):
    for i in line:
        print('#' if i else '.')

def print_matrix(matrix):
    print("Matrix size: {}x{}".format(len(matrix), len(matrix[0])))
    for i in matrix:
        print_line(i)

def get_line(matrix, i):
    if i < 0 or i >= len(matrix):
        return [False] * len(matrix[0])
    return matrix[i]

def get_v_line(matrix, i):
    if i < 0 or i >= len(matrix[0]):
        return [False] * len(matrix)
    return [x[i] for x in matrix]

def join_dots(l1, l2):
    return [l1[i] or l2[i] for i in range(len(l1))]

def flip_h(matrix, line):
    size = len(matrix)
    rest = size - line - 1
    new_size = max(line, rest)
    new_matrix = []
    for i in range(new_size):
        new_matrix.append([])
    for i in range(new_size):
        new_pos = new_size - i - 1
        h1 = line - i - 1
        h2 = line + i + 1
        lineh1 = get_line(matrix, h1)
        lineh2 = get_line(matrix, h2)
        new_line = join_dots(lineh1, lineh2)
        new_matrix[new_pos] = new_line
    return new_matrix

def fill_col(matrix, i, l):
    for j in range(len(matrix)):
        matrix[j][i] = l[j]

def flip_v(matrix, line):
    size = len(matrix[0])
    rest = size - line - 1
    new_size = max(line, rest)
    new_matrix = []
    for i in range(len(matrix)):
        new_matrix.append([False] * new_size)
    for i in range(new_size):
        new_pos = new_size - i - 1
        h1 = line - i - 1
        h2 = line + i + 1
        lineh1 = get_v_line(matrix, h1)
        lineh2 = get_v_line(matrix, h2)
        new_line = join_dots(lineh1, lineh2)
        fill_col(new_matrix, new_pos, new_line)
    return new_matrix

def count_dots(matrix):
    return functools.reduce(lambda a, x: a + (1 if x else 0), [item for sublist in matrix for item in sublist], 0)

matrix, insts = read_input()
i = 0
for inst in insts:
    if inst[0] == 'y':
        matrix = flip_h(matrix, inst[1])
    else:
        matrix = flip_v(matrix, inst[1])
    i = i + 1
    print("Iteration", i, ":", count_dots(matrix))
print_matrix(matrix)
