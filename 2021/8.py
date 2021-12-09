from enum import Enum
import functools

def read_input():
    f = open("8.txt", "r")
    line = f.readline().replace("\n", "")
    nos = []
    while len(line) > 0:
        parts = line.split(" | ")
        nos.append([parts[0].split(" "), parts[1].split(" ")])
        line = f.readline().replace("\n", "")
    return nos

class Position(Enum):
    UP = 1
    LUP = 2
    RUP = 3
    MID = 4
    LDOWN = 5
    RDOWN = 6
    DOWN = 7

available = "abcdefg"

numbers = {
    0: [Position.UP, Position.LUP, Position.RUP, Position.RDOWN, Position.LDOWN, Position.DOWN],
    1: [Position.RUP, Position.RDOWN],
    2: [Position.UP, Position.RUP, Position.MID, Position.LDOWN, Position.DOWN],
    3: [Position.UP, Position.RUP, Position.MID, Position.RDOWN, Position.DOWN],
    4: [Position.LUP, Position.MID, Position.RUP, Position.RDOWN],
    5: [Position.UP, Position.LUP, Position.MID, Position.RDOWN, Position.DOWN],
    6: [Position.UP, Position.LUP, Position.MID, Position.RDOWN, Position.LDOWN, Position.DOWN],
    7: [Position.UP, Position.RUP, Position.RDOWN],
    8: [Position.UP, Position.LUP, Position.RUP, Position.MID, Position.LDOWN, Position.RDOWN, Position.DOWN],
    9: [Position.UP, Position.LUP, Position.RUP, Position.MID, Position.RDOWN, Position.DOWN]
}

def get_positions(length):
    if length == 2:
        return [numbers[1]]
    if length == 3:
        return [numbers[7]]
    if length == 4:
        return [numbers[4]]
    if length == 5:
        return [numbers[2], numbers[3], numbers[5]]
    if length == 6:
        return [numbers[0], numbers[6], numbers[9]]
    return [numbers[8]]

def apply(conf, remain, positions):
    if len(remain) == 0:
        return [conf]
    if remain[0] in conf:
        if conf[remain[0]] in positions:
            newpos = [x for x in positions if x != conf[remain[0]]]
            return apply(conf, remain[1:], newpos)
        return None
    valid = []
    for pos in positions:
        newconf = conf.copy()
        newconf[remain[0]] = pos
        newpos = [x for x in positions if x != pos]
        final = apply(newconf, remain[1:], newpos)
        if final is not None:
            valid = valid + final
    return valid

def apply_all(words):
    words.sort(key = lambda x: len(x))
    confs = [{}]
    for word in words:
        oldconfs = confs
        confs = []
        for pos in get_positions(len(word)):
            for conf in oldconfs:
                valid_confs = apply(conf, word, pos)
                if valid_confs is not None:
                    confs.extend(valid_confs)
    return confs[0]

def get(digit, conf):
    dashes = [conf[x] for x in digit]
    for key in numbers:
        if len(dashes) == len(numbers[key]):
            pending = [x for x in dashes if x not in numbers[key]]
            if len(pending) == 0:
                return str(key)
    return None

def solve(digits, conf):
    return int(functools.reduce(lambda x, y: x + get(y, conf), digits, ""))

input = read_input()
suma = 0
for l in input:
    conf = apply_all(l[0])
    suma = suma + solve(l[1], conf)

print("Result:", suma)

