import re

def read_line(input):
    line = input.readline().replace('\n', '')
    return line.split()

def read(input):
    passport = {}
    line = read_line(input)
    while len(line) > 0:
        for element in line:
            parts = element.split(':')
            passport[parts[0]] = parts[1]
        line = read_line(input)
    return passport

def is_valid_hair(value):
    match_cm = re.search("([0-9]+)cm", value)
    if match_cm:
        return 150 <= int(match_cm.group(1)) <= 193
    match_in = re.search("([0-9]+)in", value)
    if match_in:
        return 59 <= int(match_in.group(1)) <= 76
    return False

validations = [
    lambda x: 1920 <= int(x["byr"]) <= 2002,
    lambda x: 2010 <= int(x["iyr"]) <= 2020,
    lambda x: 2020 <= int(x["eyr"]) <= 2030,
    lambda x: is_valid_hair(x["hgt"]),
    lambda x: re.search("#[0-9a-f]{6}", x["hcl"]),
    lambda x: x["ecl"] in "amb blu brn gry grn hzl oth".split(),
    lambda x: re.search("[0-9]{9}", x["pid"])
]

required = "byr iyr eyr hgt hcl ecl pid".split()

def is_valid(passport):
    for i in required:
        if i not in passport:
            return False
    for i in validations:
        if not i(passport):
            return False
    return True

f = open("4-1-input.txt", "r")

total = 0
correct = 0
passport = read(f)
while passport:
    total = total + 1
    if is_valid(passport):
        correct = correct + 1
    passport = read(f)

f.close()

print(correct)
print(total)
