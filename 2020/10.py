from functools import reduce

def read_input(input):
    f = open(input, "r")

    numbers = [0]
    line = f.readline().replace('\n', '')
    while line:
        numbers.append(int(line))
        line = f.readline().replace('\n', '')

    f.close()

    numbers.sort()
    numbers.append(numbers[-1] + 3)
    return numbers

input = read_input("10-input.txt")
size = len(input)

def is_valid(current, next, index):
    return next >= 0 and index[next] - index[current] >= 3

def count_options(input, options, pos):
    options[pos] = 0
    next = pos + 1
    while next < size and input[pos] >= input[next] - 3:
        options[pos] = options[pos] + options[next]
        next = next + 1

options = [0 for i in range(0, size)]
options[size - 1] = 1
for i in range(1, size):
    count_options(input, options, size - i - 1)

print(options)
print(options[0])
