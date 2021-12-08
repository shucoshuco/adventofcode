import copy

def read_input(input):
    f = open(input, "r")

    grid = [[]]
    char = f.read(1)
    line = 0
    while char:
        if char == '\n':
            grid.append([])
            line = line + 1
        else:
            grid[line].append(char)
        char = f.read(1)
    return grid

def is_valid(grid, row, col):
    return 0 <= row < len(grid) and col >= 0 and col < len(grid[row])

def next_seat(grid, row, col, row_step, col_step):
    next_row = row + row_step
    next_col = col + col_step
    while is_valid(grid, next_row, next_col) and grid[next_row][next_col] == '.':
        next_row = next_row + row_step
        next_col = next_col + col_step
    if not is_valid(grid, next_row, next_col):
        return '.'
    return grid[next_row][next_col]

def sum_adjacents(grid, row, col):
    sum = 0
    for x in range(-1, 2):
        for y in range(-1, 2):
            if (x != 0 or y != 0) and next_seat(grid, row, col, x, y) == '#':
                sum = sum + 1
    return sum

def next_state(grid, row, col):
    if grid[row][col] == '.':
        return '.'
    sum = sum_adjacents(grid, row, col)
    if sum == 0:
        return '#'
    if sum >= 5:
        return 'L'
    return grid[row][col]

def execute(grid):
    sum = 0
    new_grid = copy.deepcopy(grid)
    for row in range(0, len(grid)):
        for col in range(0, len(grid[row])):
            new_grid[row][col] = next_state(grid, row, col)
            if new_grid[row][col] != grid[row][col]:
                sum = sum + 1
    return sum, new_grid

input = read_input("11-input.txt")
changes, input = execute(input)
passes = 1
while changes:
    changes, input = execute(input)
    passes = passes + 1

occupied = 0
for i in input:
    for j in i:
        if j == '#':
            occupied = occupied + 1
print(passes)
print(occupied)

