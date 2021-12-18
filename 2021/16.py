import sys
import functools

def next(chain):
    ptype = chain[3:6]
    if ptype == "100":
        pkg = NumberPacket(chain[0:6])
    else:
        pkg = OpPacket(chain[0:6])
    chain = pkg.read(chain[6:])
    return chain, pkg

class Packet:

    def __init__(self, chars):
        self.version = chars[:3]
        self.ptype = chars[3:]

    def get_version(self):
        return int(self.version, 2)


class NumberPacket(Packet):

    def __init__(self, chars):
        Packet.__init__(self, chars)

    def read(self, chain):
        i = 0
        number = ""
        while chain[i] == "1":
            number = number + chain[i + 1: i + 5]
            i = i + 5
        number = number + chain[i + 1: i + 5]
        self.number = int(number, 2)
        self.long = 6 + i + 5
        return chain[i + 5:]

    def get_version_sum(self):
        return self.get_version()

    def calculate(self):
        return self.number

def ends(chain):
    return len(chain) == 0 or int(chain, 2) == 0

class OpPacket(Packet):

    ops = {
            "000": lambda pkgs: functools.reduce(lambda a, b: a + b.calculate(), pkgs, 0),
            "001": lambda pkgs: functools.reduce(lambda a, b: a * b.calculate(), pkgs, 1),
            "010": lambda pkgs: functools.reduce(lambda a, b: min(a, b.calculate()), pkgs, 1000000000),
            "011": lambda pkgs: functools.reduce(lambda a, b: max(a, b.calculate()), pkgs, 0),
            "101": lambda pkgs: 1 if pkgs[0].calculate() > pkgs[1].calculate() else 0,
            "110": lambda pkgs: 1 if pkgs[0].calculate() < pkgs[1].calculate() else 0,
            "111": lambda pkgs: 1 if pkgs[0].calculate() == pkgs[1].calculate() else 0
    }

    def __init__(self, chars):
        Packet.__init__(self, chars)

    def read_bits(self, chain):
        length = int(chain[0:15], 2)
        self.packages = []
        chain = chain[15:]
        orig = len(chain)
        while orig - len(chain) < length:
            chain, pck = next(chain)
            self.packages.append(pck)
        return chain

    def read_pck(self, chain):
        length = int(chain[0:11], 2)
        self.packages = []
        chain = chain[11:]
        for i in range(length):
            chain, pck = next(chain)
            self.packages.append(pck)
        return chain

    def read(self, chain):
        print("Chain2", chain)
        if chain[0] == "0":
            return self.read_bits(chain[1:])
        return self.read_pck(chain[1:])

    def get_version_sum(self):
        return functools.reduce(lambda a, b: a + b.get_version_sum(), self.packages, int(self.version, 2))

    def calculate(self):
        return self.ops[self.ptype](self.packages)


def read_input():
    f = open("16.txt", "r")
    line = [l.replace("\n", "") for l in f.readlines()]
    f.close()
    return line

def to_bin(hexa):
    binv = ""
    for i in hexa:
        binv = binv + format(int(i, 16), "04b")
    return binv

def next(chain):
    ptype = chain[3:6]
    if ptype == "100":
        pkg = NumberPacket(chain[0:6])
    else:
        pkg = OpPacket(chain[0:6])
    chain = pkg.read(chain[6:])
    return chain, pkg

def process(chain):
    pkgs = []
    while not ends(chain):
        print("Chain", chain)
        chain, pkg = next(chain)
        pkgs.append(pkg)

    return pkgs

for i in read_input():
    print("--------------------------------------")
    print(i)
    chain = to_bin(i)
    print(chain)
    pks = process(chain)
    print(len(pks))
    print("Versions:", functools.reduce(lambda a, b: a + b.get_version_sum(), pks, 0))
    print("Calculation:", pks[0].calculate())


