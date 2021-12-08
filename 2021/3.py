import os

def read_input():
    f = open("3.txt", "r")

    data = []

    line = f.readline()
    while len(line) > 0:
        data.append(line.replace("\n", ""))
        line = f.readline()

    f.close()

    return data

def count(lines, pos):
    ones = 0
    for l in lines:
        if l[pos] == "1":
            ones = ones + 1
    if ones == len(lines) / 2:
            return "-"
    return "1" if ones > (len(lines) / 2) else "0"

def get_number(lines):
    size = len(lines[0])
    number = ""
    for i in range(size):
        number = number + count(lines, i)
    return number

def filter(lines, pos, ones):
    ref = get_number(lines)[pos]
    print("Ref:", ref)
    if ref == "-":
        search = "1" if ones else "0"
    elif ref == "1":
        search = "1" if ones else "0"
    else:
        search = "0" if ones else "1"
    return [l for l in lines if l[pos] == search]


def apply(lines, pos, ones):
    print("Checking lines:", lines)
    if len(lines) == 1:
        return lines[0]
    if len(lines) == 0 or pos > len(lines[0]):
        return None
    return apply(filter(lines, pos, ones), pos + 1, ones)

lines = read_input()
o2 = apply(lines, 0, True)
print("O2:", o2, " / ", int(o2, 2))
co2 = apply(lines, 0, False)
print("CO2:", co2, " / ", int(co2, 2))

print("Number:", int(o2, 2) * int(co2, 2))
