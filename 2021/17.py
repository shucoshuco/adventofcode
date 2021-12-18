import sys
import functools

def read_input():
    f = open("17-ex.txt", "r")
    parts = f.readline().replace("\n", "").split(" ")
    x = [int(c) for c in parts[2][2:][:-1].split("..")]
    y = [int(c) for c in parts[3][2:].split("..")]
    f.close()
    return x, y

def throw(target_x, target_y, vx, vy):
    posx = 0
    posy = 0
    max_posy = 0
    passed = False
    points = []
    cvx = vx
    cvy = vy
    first = True
    while posy >= target_y[0]:
        posx = posx + cvx
        posy = posy + cvy
        points.append([posx, posy])
        if posy > max_posy:
            max_posy = posy
        if posx >= target_x[0] and posx <= target_x[1] and posy >= target_y[0] and posy <= target_y[1]:
            return 0, max_posy, points
        if posx > target_x[1]:
            return 1 if first or posy >= target_y[1] else -1, max_posy, points
        if cvx > 0:
            cvx = cvx - 1
        elif cvx < 0:
            cvx = cvx + 1
        cvy = cvy = cvy - 1
        first = False
    return -1, max_posy, points

def print_throw(target_x, target_y, points):
    row = functools.reduce(lambda a, b: max(a, b), [x[1] for x in points], 0)
    limit_x = functools.reduce(lambda a, b: max(a, b), [x[0] for x in points], target_x[1]) + 2
    limit_y = functools.reduce(lambda a, b: min(a, b), [x[1] for x in points], target_y[0]) - 1
    print(target_x)
    print(target_y)
    print(points)
    matrix = []
    while row >= limit_y:
        txt = "{}\t--> ".format(row)
        for x in range(limit_x):
            if x == 0 and row == 0:
                txt = txt + 'S'
            elif [x, row] in points:
                txt = txt + '#'
            elif x >= target_x[0] and x <= target_x[1] and row >= target_y[0] and row <= target_y[1]:
                txt = txt + 'T'
            else:
                txt = txt + '.'
        matrix.append(txt)
        row = row - 1
    for i in matrix:
        print(i)

def process(target_x, target_y):
    hits = []
    initvx = target_x[0]
    for i in range(abs(target_y[0] * 2)):
            vy = target_y[0] + i
            vx = 1
            goal, y, points = throw(target_x, target_y, vx, vy)
            while goal <= 0:
                if goal == 0:
                    hits.append([vx, vy, y, points])
                vx = vx + 1
                goal, y, points = throw(target_x, target_y, vx, vy)
    return hits

x, y = read_input()
hits = process(x, y)
print("Highest:", functools.reduce(lambda a, b: max(a, b), [i[2] for i in hits], 0))
print("Number of hits:", len(hits))

