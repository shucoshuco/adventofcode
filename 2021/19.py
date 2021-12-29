import sys
import functools
import math
import time
from scipy.spatial import distance

class Scanner:

    def __init__(self, scannid, points):
        self.id = scannid
        self.points = points
        self.calculate_distances()

    def __str__(self):
        return "{}: {}".format(self.id, self.points)

    def calculate_distances(self):
        self.distances = {}
        for i in range(len(self.points) - 1):
            for j in range(len(self.points) - i - 1):
                dist = distance.euclidean(self.points[i], self.points[i + j + 1])
                if dist in self.distances:
                    raise ValueError("Distance duplicated!!!!")
                self.distances[dist] = (self.points[i], self.points[i + j + 1])

    def get_distances(self):
        return self.distances.copy()

    def extend(self, points):
        print("Extend with", points)
        for p in points:
            if p not in self.points:
                self.points.append(p)
        self.calculate_distances()

def read_scanner(f):
    header = f.readline().replace("\n", "")
    if len(header) == 0:
        return None
    scannid = header.split(" ")[2]
    points = []
    point = f.readline().replace("\n", "")
    while len(point) > 0:
        points.append([int(i) for i in point.split(",")])
        point = f.readline().replace("\n", "")
    return Scanner(scannid, points)

def read_input():
    f = open("19-ex.txt", "r")
    scanners = []
    scanner = read_scanner(f)
    while scanner is not None:
        scanners.append(scanner)
        scanner = read_scanner(f)
    f.close()
    return scanners

def normalize(p1, p2):
    return (p2[0] - p1[0], p2[1] - p1[1], p2[2] - p1[2])

def calculate_rotation(d1, d2):
    d1norm = normalize(d1[0], d1[1])
    d2norm = normalize(d2[0], d2[1])
    return [
            d2norm[0] / d1norm[0],
            d2norm[1] / d1norm[1],
            d2norm[2] / d1norm[2],
    ]

def intersection(scanner1, scanner2):
    d1 = scanner1.get_distances()
    d2 = scanner2.get_distances()
    diff = [x for x in d1 if x in d2]
    if len(diff) >= 66:
        ref = diff[0]
        return calculate_rotation(d1[ref], d2[ref])
    return None

def get_pairs(scanners):
    pairs = []
    for i in range(len(scanners) - 1):
        for j in range(len(scanners) - i - 1):
            rotation = intersection(scanners[i], scanners[i + j + 1])
            if rotation is not None:
                pairs.append((scanners[i].id, scanners[i + j + 1].id, rotation))
    return pairs

def get_pair(scid, pairs):
    for i in pairs:
        if i[1] == scid:
            return i
    raise ValueError("Pair not found!!!")

def get_scanner(scid, scanners):
    for i in scanners:
        if i.id == scid:
            return i
    raise ValueError("Scanner not found!!!")

def extend(sc1, sc2, pairs, scanners):
    points = sc2.points.copy()
    while True:
        pair = get_pair(sc2.id, pairs)
        points = [(p[0] * pair[2][0], p[1] * pair[2][1], p[2] * pair[2][2]) for p in points]
        if pair[0] == sc1.id:
            sc1.extend(points)
            return
        sc2 = get_scanner(pair[0], scanners)

scanners = read_input()
pairs = get_pairs(scanners)

extend(scanners[0], scanners[1], pairs, scanners)

print(scanners[0].points)