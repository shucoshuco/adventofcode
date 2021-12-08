import re

def valid(password, letter, index):
    return index < len(password) + 1 and password[index - 1] == letter

f = open("2-1-input.txt", "r")

line = f.readline()
right = 0
while line:
    match = re.search("([0-9]+)-([0-9]+) ([a-z]): ([a-z]+)", line)
    min = int(match.group(1))
    max = int(match.group(2))
    letter = match.group(3)
    password = match.group(4)
    if (valid(password, letter, min) and not valid(password, letter, max)) or (valid(password, letter, max) and not valid(password, letter, min)):
        print("Right: {}".format(match.group()))
        right = right + 1
    line = f.readline()

print(right)
