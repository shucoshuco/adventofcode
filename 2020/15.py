
input = [int(x) for x in "0,13,16,17,1,10,6".split(",")]

list = {}

def push(i, value):
    if not i in list:
        list[i] = []
    list[i] = [value] + list[i][:1]
    if len(list[i]) > 1:
        return list[i][0] - list[i][1]
    return 0

i = 0
while i < len(input) - 1:
    push(input[i], i + 1)
    i = i +1

i = len(input)
last = input[i - 1]
while i < 30000000:
    last = push(last, i)
    i = i +1
    if i % 10000 == 0:
        print(i)

print(last)
