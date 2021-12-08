import re
import math
from functools import reduce

mask_re = "mask = ([01X]+)"
mem_re = "mem\[([0-9]+)\] = ([0-9]+)"

mems = {}

def setBit(int_type, offset):
    mask = 1 << offset
    return int_type | mask

def clearBit(int_type, offset):
    mask = ~(1 << offset)
    return int_type & mask

def floating(value, mask, start):
    start = mask.find('X', start)
    if start >= 0:
        pos = len(mask) - start - 1
        left = floating(setBit(value, pos), mask, start + 1)
        right = floating(clearBit(value, pos), mask, start + 1)
        return left + right
    else:
        return [value]

def apply_mask(value, mask):
    or_op = int(mask.replace('X', '0'), 2)
    return [x | or_op for x in floating(value, mask, 0)]

def parse_line(current_mask, line):
    mask = re.search(mask_re, line)
    if mask:
        return mask.group(1)
    mem = re.search(mem_re, line)
    if mem:
        for address in  apply_mask(int(mem.group(1)), current_mask):
            mems[address] = int(mem.group(2))
    return current_mask

f = open("14-input.txt")
line = f.readline()
current_mask = "X"
while line:
    current_mask = parse_line(current_mask, line)
    line = f.readline()


print(reduce(lambda x, value: x + value, mems.values(), 0))
