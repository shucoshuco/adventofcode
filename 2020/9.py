def read_input(input):
    f = open(input, "r")

    numbers = []
    line = f.readline().replace('\n', '')
    while line:
        numbers.append(int(line))
        line = f.readline().replace('\n', '')

    f.close()

    return numbers

def is_valid(input, index, window):
    for i in range(index - window, index - 1):
        for j in range(i + 1, index):
            if input[i] + input[j] == input[index]:
                return True
    return False

def execute(input, window):
    for i in range(window, len(input)):
        if not is_valid(input, i, window):
            return input[i]

def search(input, value):
    for i in range(0, len(input)):
        j = i + 1
        sum = input[i]
        lower = input[i]
        largest = input[i]
        while sum < value:
            sum = sum + input[j]
            lower = min(lower, input[j])
            largest = max(largest, input[j])
            j = j + 1
        if sum == value:
            return lower + largest
    return False

input = read_input("9-input.txt")
v = execute(input, 25)
print(search(input, v))
