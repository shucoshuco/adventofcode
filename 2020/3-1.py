import re

def is_tree(line, position):
    fixed = line.replace('\n', '')
    length = len(fixed)
    index = position % length
    return fixed[index] == '#'

def count_trees(move, down):
    f = open("3-1-input.txt", "r")

    f.readline()
    for i in range(0, down):
        line = f.readline()
    trees = 0
    right = move
    total_lines = 0
    while line:
        if is_tree(line, right):
            trees = trees + 1
        for i in range(0, down):
            line = f.readline()
        right = right + move
        total_lines = total_lines + 1

    f.close()

    print(trees)
    print(total_lines)

    return trees

print(count_trees(1, 1) * count_trees(3, 1) * count_trees(5, 1) * count_trees(7, 1) * count_trees(1, 2))
