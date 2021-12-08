import re

def read_line(input):
    return input.readline().replace('\n', '')

def read(input):
    answers = {}
    line = read_line(input)
    if not line:
        return -1
    for letter in line:
        answers[letter] = True
    line = read_line(input)
    while len(line) > 0:
        to_remove = []
        for valid in answers.keys():
            if not valid in line:
                to_remove.append(valid)
        for valid in to_remove:
            del answers[valid]
        line = read_line(input)
    return len(answers.keys())

f = open("6-input.txt", "r")

sum = 0
group = read(f)
while group >= 0:
    sum = sum + group
    group = read(f)

f.close()

print(sum)
