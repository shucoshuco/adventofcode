import copy

def build_id(z, y, x, w):
    return "{},{},{},{}".format(z, y, x,w)

def debuild_id(id):
    return [int(x) for x in id.split(",")]

def read_input(input):
    f = open(input, "r")

    grid = {}
    char = f.read(1)
    z = 0
    y = 0
    x = 0
    w = 0
    while char:
        if char == '\n':
            y = y + 1
            x = 0
        else:
            if char == '#':
                grid[build_id(z, y, x, w)] = True
            x = x + 1
        char = f.read(1)
    return grid

def is_active(grid, pos):
    return pos in grid and grid[pos]

def get_neighbors(pos):
    cords = debuild_id(pos)
    neighbors = []
    for z in range(-1, 2):
        for y in range(-1, 2):
            for x in range(-1, 2):
                for w in range(-1, 2):
                    if z != 0 or y != 0 or x != 0 or w != 0:
                        neighbors.append(build_id(cords[0] + z, cords[1] + y, cords[2] + x, cords[3] + w))
    return neighbors

def sum_active(grid, neighbors):
    sum = 0
    for i in neighbors:
        if is_active(grid, i):
            sum = sum + 1
    return sum

def sum_adjacents(grid, pos):
    return sum_active(grid, get_neighbors(pos))

def check_not_active(grid, i):
    return not is_active(grid, i) and sum_adjacents(grid, i) == 3

def execute(grid):
    next_grid = {}
    visited = {}
    for i in grid:
        neighbors = get_neighbors(i)
        sum = sum_active(grid, neighbors)
        if sum in [2, 3]:
            next_grid[i] = True
        visited[i] = True
        for j in [x for x in neighbors if not is_active(grid, x) and x not in visited]:
            if check_not_active(grid, j):
                next_grid[j] = True
            visited[j] = True
    return next_grid

grid = read_input("17-input.txt")
print(grid)

for i in range(0, 6):
    grid = execute(grid)
    print(grid)

occupied = len(grid)

print(occupied)
