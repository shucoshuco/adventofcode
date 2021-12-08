import os

def parse_cmd(command):
    parts = command.split(' ')
    if parts[0] == "forward":
        return [int(parts[1]), 0]
    if parts[0] == "down":
        return [0, int(parts[1])]
    return [0, -int(parts[1])]

def read_input():
    f = open("2.txt", "r")

    data = []

    line = f.readline()
    while len(line) > 0:
        data.append(parse_cmd(line))
        line = f.readline()

    f.close()

    return data

def execute(commands):
    x = 0
    y = 0
    aim = 0
    for cmd in commands:
        if cmd[0] == 0:
            aim = aim + cmd[1]
        else:
            x = x + cmd[0]
            y = y + cmd[0] * aim
    return x * y

print("Final:", execute(read_input()))
