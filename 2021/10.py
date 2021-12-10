import functools

def read_input():
    f = open("10.txt", "r")
    lines = f.readlines()
    return [l.replace("\n", "") for l in lines]

opens = ['(', '[', '{', '<']
closes = [')', ']', '}', '>']

def get_open(close):
    for idx, char in enumerate(closes):
        if char == close:
            return opens[idx]
    raise ValueError("No valid open for close '{}'".format(close))

def get_close(open):
    for idx, char in enumerate(opens):
        if char == open:
            return closes[idx]
    raise ValueError("No valid close for open '{}'".format(open))

def check(line):
    stack = []
    for l in line:
        if l in opens:
            stack.append(l)
        elif l in closes:
            if stack[-1] == get_open(l):
                stack.pop()
            else:
                return -1, stack, l
    return 0, stack, None

count = {
        ')': 1,
        ']': 2,
        '}': 3,
        '>': 4
}

def complete(line):
    return functools.reduce(lambda a, b: a * 5 + count[b], [get_close(x) for x in line[::-1]], 0)

def iterate(lines):
    suma = 0
    results = []
    for l in lines:
        r, stack, c = check(l)
        if r == 0 and len(stack) > 0: 
            results.append(complete(stack))
    results.sort()
    return results[int(len(results) / 2)]

lines = read_input()
print(iterate(lines))

