import re

op_regex = r'([a-z]{3}) ([+-][0-9]+)'

executor = {
    "nop": lambda x: (1, 0),
    "acc": lambda x: (1, x),
    "jmp": lambda x: (x, 0)
}

def execute_op(input):
    return executor.get(input["op"])(input["v"])

def read_input():
    f = open("8-input.txt", "r")

    operations = []
    line = f.readline().replace('\n', '')
    while line:
        op_match = re.search(op_regex, line)
        operations.append({"op": op_match.group(1), "v": int(op_match.group(2))})
        line = f.readline().replace('\n', '')

    f.close()

    return operations

def switch(input, line):
    if input[line]["op"] == "nop":
        new_input = input.copy()
        new_input[line]["op"] = "jmp"
        return new_input
    if input[line]["op"] == "jmp":
        new_input = input.copy()
        new_input[line]["op"] = "nop"
        return new_input
    return False


def execute(input, acc, ex_line, visited_lines):
    if ex_line in visited_lines:
        return False, acc
    if ex_line >= len(input):
        return True, acc
    visited_lines.append(ex_line)
    l, a = execute_op(input[ex_line])
    next_ex_line = ex_line + l
    next_acc = acc + a
    result, r = execute(input, next_acc, next_ex_line, visited_lines.copy())
    if not result:
        new_input = switch(input, next_ex_line)
        if new_input:
            result, r = execute(new_input, next_acc, next_ex_line, visited_lines.copy())
    return result, r

print(execute(read_input(), 0, 0, []))
