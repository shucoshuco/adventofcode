import re

key_regex = r'([a-z]+ [a-z]+) bags contain'
value_regex = r'([0-9]+) ([a-z]+ [a-z]+) bags?'

def parse_line(input):
    key_match = re.search(key_regex, input)
    contents = {}
    for values in re.finditer(value_regex, input):
        contents[values.group(2)] = int(values.group(1))

    return key_match.group(1), contents

def build_dict(input):
    rules = {}
    line = input.readline().replace('\n', '')
    while line:
        key, contains = parse_line(line)
        rules[key] = contains
        line = input.readline().replace('\n', '')
    return rules

def count_bags(dict, key):
    sum = 1
    for bag in dict[key].keys():
        sum = sum + count_bags(dict, bag) * dict[key][bag]
    return sum

f = open("7-input.txt", "r")

rules = build_dict(f)
f.close()

valid = {"shiny gold": True}
last_len = 0
while len(valid.keys()) != last_len:
    last_len = len(valid.keys())
    for i in rules.keys():
        test = list(valid.keys())
        for j in test:
            if j in rules[i]:
                valid[i] = True

print(valid)
print(len(valid.keys()))

print(count_bags(rules, "shiny gold"))
