import math
import copy
import re

tile_re = "Tile ([0-9]+):"

def rotate(input):
    return {
        "top": input["left"][::-1],
        "right": input["top"],
        "bottom": input["right"][::-1],
        "left": input["bottom"]
    }

def hor_flip(input):
    return {

        "top": input["bottom"],
        "right": input["right"][::-1],
        "bottom": input["top"],
        "left": input["left"][::-1]
    }

def ver_flip(input):
    return {
        "top": input["top"][::-1],
        "right": input["left"],
        "bottom": input["bottom"][::-1],
        "left": input["right"]
    }

def build_combinations(input):
    return [input, hor_flip(input), ver_flip(input)]

def build_all_combinations(input):
    last = input
    all = []
    for _ in range(0, 4):
        all.extend(build_combinations(last))
        last = rotate(last)
    return all

def read_tile(f):
    tile = f.readline().replace('\n', '')
    if tile == '':
        tile = f.readline().replace('\n', '')
    if not tile:
        return False
    top = f.readline().replace('\n', '')
    left = top[0]
    right = top[-1]
    last = ""
    for _ in range(0, len(top) - 1):
        last = f.readline().replace('\n', '')
        left = left + last[0]
        right = right + last[-1]
    bottom = last
    return {
        "id": re.search(tile_re, tile).group(1),
        "options": [
            top,
            bottom,
            left,
            right,
            top[::-1],
            bottom[::-1],
            left[::-1],
            right[::-1],
        ],
        "combinations": build_all_combinations({
            "top": top,
            "left": left,
            "right": right,
            "bottom": bottom
        })
    }

def read_input(f):
    tile = read_tile(f)
    result = []
    while tile:
        result.append(tile)
        tile = read_tile(f)
    return result

def build_options(input):
    options = {}
    for i in input:
        for o in i["options"]:
            if not o in options:
                options[o] = i["id"]
            elif not i["id"] in options[o]:
                options[o].append(i["id"])
    return options

def print_grid(grid):
    value = "("
    for i in grid:
        value = value + "(" + ",".join([x["id"] for x in i if x]) + "), "
    return value + ")"

def adjacents(i, j, offset, size):
    adjs = []
    for p in offset:
        if is_valid(i + p[0], j + p[1], size):
            adjs.append(p)
    return adjs

def v_adjacents(i, j, size):
    return adjacents(i, j, [[-1, 0], [1, 0], [0, 1], [0, -1]], size)

def d_adjacents(i, j, size):
    return adjacents(i, j, [[-1, -1], [1, 1], [-1, 1], [1, -1]], size)

def get_from_grid(grid, i, j, size):
    if is_valid(i, j, size):
        return grid[i][j]


def new_grid(size):
    grid = []
    for i in range(0, size):
        grid.append([])
        for _ in range(0, size):
            grid[i].append(None)
    return grid

def find_next(all, grid, i, j, used):
    top = None
    if i > 0:
        top = grid[i - 1][j]["bottom"]
    if j > 0:
        left = grid[i][j - 1]["right"]
    for op in all:
        


def iterate(all, size):
    for i in range(0, size):
        for j in range(0, size):

    i = int(size / 2)
    j = int(size / 2)
    for tile in all:
        for m in tile["combinations"]:
            grid = new_grid(size)
            grid[i][j] = {
                "id": tile["id"],
                "top": m["top"],
                "bottom": m["bottom"],
                "left": m["left"],
                "right": m["right"],
            }
            match = find_match(all, grid, size)
            if match:
                return match

    return False

f = open("20-input.txt")
input = read_input(f)

print(len(input))
size = int(math.sqrt(len(input)))
print(size)

solution = iterate(input, size)
print(int(solution[0][0]["id"]) * int(solution[0][size - 1]["id"]) * int(solution[size - 1][0]["id"]) * int(solution[size - 1][size - 1]["id"]))

