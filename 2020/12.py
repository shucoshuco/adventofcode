rotation = {
    90: lambda pos: [pos[1], -pos[0]],
    -90: lambda pos: [-pos[1], pos[0]]
}

pos = {
    'boat': [0, 0],
    'waypoint': [10, 1]
}

order = [
    [1, 0],
    [0, -1],
    [-1, 0],
    [0, 1]
]

def advance(coords, dir, steps):
    coords[0] = coords[0] + dir[0] * steps
    coords[1] = coords[1] + dir[1] * steps

def rotate(dir, grades):
    for i in range(0, int(grades / 90)):
        pos['waypoint'] = rotation[90 * dir](pos['waypoint'])

actions = {
    'F': lambda x: advance(pos['boat'], pos['waypoint'], x),
    'E': lambda x: advance(pos['waypoint'], order[0], x),
    'S': lambda x: advance(pos['waypoint'], order[1], x),
    'W': lambda x: advance(pos['waypoint'], order[2], x),
    'N': lambda x: advance(pos['waypoint'], order[3], x),
    'R': lambda x: rotate(1, x),
    'L': lambda x: rotate(-1, x),
}


input = open("12-input.txt")

line = input.readline().replace('\n', '')
while line:
    actions[line[0]](int(line[1:]))
    line = input.readline().replace('\n', '')

print(pos)
print(abs(pos['boat'][0]) + abs(pos['boat'][1]))
