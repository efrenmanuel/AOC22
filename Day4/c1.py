def setFromString(sections):
    delimiterSections = [int(s) for s in sections.split("-")]
    return set(range(delimiterSections[0], delimiterSections[1]+1))


def makeSetArrayOfLine(line):
    return [setFromString(sections) for sections in line.split(",")]


def getLineValue(line):
    sets = makeSetArrayOfLine(line)
    return sets[0].issubset(sets[1]) + sets[1].issubset(sets[0])


def getLineValue2(line):
    sets = makeSetArrayOfLine(line)
    return len(sets[0] & sets[1]) > 0


def p1():
    with open("input1.txt", "r") as inputFile:
        lines = inputFile.read().split()
        return sum(map(getLineValue, lines))


def p2():
    with open("input1.txt", "r") as inputFile:
        lines = inputFile.read().split()
        return sum(map(getLineValue2, lines))


print(p1())
print(p2())
