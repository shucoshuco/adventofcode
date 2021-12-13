import os
import functools

def read_input():
    f = open("3.txt", "r")
    data = f.readline().replace("\n", "")
    f.close()
    return data

def walk(x, y, char):
    if char == '^':
        y = y - 1
    elif char == '>':
        x = x + 1
    elif char == 'v':
        y = y + 1
    elif char == '<':
        x = x - 1
    return x, y

def inc_mapa(mapa, x, y):
    key = "{},{}".format(x, y)
    if key in mapa:
        mapa[key] = mapa[key] + 1
    else:
        mapa[key] = 1


def deliver(dirs):
    x = 0
    y = 0
    rx = 0
    ry = 0
    turn = 0
    mapa = {}
    mapa["{},{}".format(x, y)] = 1
    for i in dirs:
        if turn % 2 == 0:
            x, y = walk(x, y, i)
            inc_mapa(mapa, x, y)
        else:
            rx, ry, = walk(rx, ry, i)
            inc_mapa(mapa, rx, ry)
        turn = turn + 1
    return mapa

dirs = read_input()
mapa = deliver(dirs)
print(len(mapa))
