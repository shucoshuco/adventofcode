import functools

def read_input():
    f = open("12.txt", "r")
    lines = f.readlines()
    nodes = {}
    matrix = []
    paths = [x.replace("\n", "").split('-') for x in lines]
    for p in paths:
        if not p[0] in nodes:
            nodes[p[0]] = len(nodes)
        if not p[1] in nodes:
            nodes[p[1]] = len(nodes)
    matrix = [[False] * len(nodes) for i in range(len(nodes))]
    for p in paths:
        matrix[nodes[p[0]]][nodes[p[1]]] = True
        matrix[nodes[p[1]]][nodes[p[0]]] = True
    return nodes, matrix

def get_node(idx, nodes):
    for key in nodes:
        if nodes[key] == idx:
            return key
    raise "Not valid idx " + idx

def is_valid(node, path, visited):
    capital = functools.reduce(lambda a, b: a and b.isupper(), node, True)
    if capital or node not in path:
        return True, visited
    if visited:
        return False, True
    if node in ["start", "end"]:
        return False, False
    return True, True

def find_path(nodes, matrix, path, visited):
    if path[-1] == 'end':
        return [path]
    paths = []
    for idx, con in enumerate(matrix[nodes[path[-1]]]):
        if con:
            node = get_node(idx, nodes)
            valid, v = is_valid(node, path, visited)
            if valid:
                newpath = path.copy()
                newpath.append(node)
                paths.extend(find_path(nodes, matrix, newpath, v))
    return paths

def print_matrix(matrix):
    for i in matrix:
        print(i)

nodes, matrix = read_input()
print(nodes)
print_matrix(matrix)
paths = find_path(nodes, matrix, ["start"], False)
print(len(paths))
