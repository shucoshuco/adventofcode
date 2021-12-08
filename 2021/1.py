import os

def read_input():
    f = open("1.txt", "r")

    data = []

    line = f.readline()
    while len(line) > 0:
        data.append(int(line))
        line = f.readline()

    f.close()

    return data

def map(data):
    mapped = []
    for i in range(len(data) - 2):
        mapped.append(data[i] + data[i + 1] + data[i + 2])
    return mapped

def calculate(data):
    increments = 0
    for i in range(len(data) - 1):
        if data[i] < data[i + 1]:
            increments = increments + 1
    return increments

print("Increments:", calculate(map(read_input())))
