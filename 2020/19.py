def read_rule(input):
    line = input.readline().replace('\n', '')
    if line == '':
        return False, False
    colon = line.index(':')
    rule_number = int(line[0:colon])
    if line[colon + 2] == '"':
        return rule_number, {
            "v": line[colon + 3:-1]
        }
    else:
        ors = line[colon + 1:].split('|')
        return rule_number, {
            "r": [[int(x) for x in parts.strip().split(' ')] for parts in ors]
        }

def positions(rule, input, i, letters):
    all_pos = []
    for j in i:
        if j < len(input):
            if "v" in rule:
                if input[j] == rule["v"]:
                    all_pos.extend([j + 1])
            elif letters <= len(input):
                poses = []
                for g in rule["r"]:
                    next = [j]
                    for r in g:
                        next = positions(rules[r], input, next, letters + len(g))
                    poses.extend(next)
                all_pos.extend(poses)
    return all_pos

input = open("19-input.txt")

rules = {}
rule, value = read_rule(input)
while value:
    rules[rule] = value
    rule, value = read_rule(input)

print(1)

max_len = 0
all_to_check = []
to_check = input.readline().replace('\n', '')
valids = 0
while to_check:
    print("Checking {}".format(to_check))
    result = positions(rules[0], to_check, [0], 0)
    if len(to_check) in result:
        valids = valids + 1
    to_check = input.readline().replace('\n', '')

print(valids)