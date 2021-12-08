import os

class Board:
    def __init__(self, f):
        self.board = []
        self.hits = []
        self.completed = False
        for i in range(5):
            self.board.append([int(x) for x in f.readline().split(" ") if x != ""])
            self.hits.append([False for x in range(5)])
        
    def apply_number(self, number):
        if self.completed:
            return False
        for i in range(5):
            for j in range(5):
                if self.board[i][j] == number:
                    self.hits[i][j] = True
        self.print()
        return self.check()

    def check(self):
        for i in range(5):
            allH = True
            allV = True
            for j in range(5):
                allH = allH and self.hits[i][j]
                allV = allV and self.hits[j][i]
            if allH or allV:
                self.completed = True
                return True
        return False

    def calculate(self):
        result = 0
        for i in range(5):
            for j in range(5):
                if not self.hits[i][j]:
                    result = result + self.board[i][j]
                    print("Adding", self.board[i][j], "=", result)
        return result

    def print(self):
        print("-------")
        print(self.board)
        print(self.hits)


def read_input():
    f = open("4.txt", "r")
    seq = [int(x) for x in f.readline().split(",") if x != ""]
    boards = []
    blank = f.readline()
    while blank:
        boards.append(Board(f))
        blank = f.readline()

    f.close()
    return seq, boards
    return None

def next(value, boards):
    return None

seq, boards = read_input()
print(seq)
completed = 0
for v in seq:
    print("Applying", v)
    for b in boards:
        if b.apply_number(v):
            if completed == len(boards) - 1:
                sol = b.calculate()
                print(sol)
                print(v)
                print("Solution:", sol * v)
                exit()
            else:
                completed = completed + 1

print("Done")
