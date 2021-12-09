import os

def get_seq(x1, x2):
    if x1 == x2:
        return [x1]
    if x1 < x2:
        return [x1 + x for x in range(x2 - x1 + 1)]
    return [x1 - x for x in range(x1 - x2 + 1)]

def get_line(p1, p2, only_hv = False):
    seqx = get_seq(p1[0], p2[0])
    seqy = get_seq(p1[1], p2[1])
    if only_hv and len(seqx) > 1 and len(seqy) > 1:
        return None
    if len(seqx) == 1:
        seqx = seqx * len(seqy)
    if len(seqy) == 1:
        seqy = seqy * len(seqx)
    result = []
    for i in range(len(seqx)):
        result.append([seqx[i], seqy[i]])
    return result
        
def fill_map(themap, line):
    for l in line:
        themap[l[1]][l[0]] = themap[l[1]][l[0]] + 1

def print_map(themap):
    print("-" * 40)
    for i in themap:
        print(i, "\t")


def read_map(size):
    f = open("5.txt", "r")
    l = f.readline().replace("\n", "");
    themap = [[0] * size for i in range(size)]
    while l != "":
        parts = l.split(" ")
        point1 = [int(x) for x in parts[0].split(",")]
        point2 = [int(x) for x in parts[2].split(",")]
        line = get_line(point1, point2)
        if line is not None:
            fill_map(themap, line)
        l = f.readline().replace("\n", "");

    return themap


def count(themap):
    suma = 0
    for i in themap:
        suma = suma + sum(1 for x in i if x > 1)
    return suma
            
themap = read_map(1000)
print("The count:", count(themap))
