import math

def get_range(start, end, letter):
    if letter in ["F", "L"]:
        return start, start + math.floor((end - start) / 2)
    return start + math.floor((end - start) / 2 + 1), end

def get_full_position(input):
    index = 0
    start = 0
    end = 127
    while start != end:
        start, end = get_range(start, end, input[index])
        index = index + 1
    row = start
    start = 0
    end = 7
    while start != end:
        start, end = get_range(start, end, input[index])
        index = index + 1
    return row * 8 + start

f = open("5-input.txt", "r")

size = 127 * 8 + 7
matrix = [False for y in range(0, size)]

boarding = f.readline().replace('\n', '')
total = 0
max_value = 0
while boarding:
    total = total + 1
    id = get_full_position(boarding)
    max_value = max(id, max_value)
    matrix[id] = True
    boarding = f.readline().replace('\n', '')

f.close()

print(max_value)
print(total)

for i in range(1, size - 2):
    if matrix[i - 1] and matrix[i + 1] and not matrix[i]:
        print(i)
