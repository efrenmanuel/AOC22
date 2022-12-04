def setFromString(sections):
    delimiterSections = [int(s) for s in sections.split("-")]
    return set(range(delimiterSections[0], delimiterSections[1]+1))


def setArrayOfLine(line):
    return [setFromString(sections) for sections in line.split(",")]


def getLineSectionsContainOther(line):
    sets = setArrayOfLine(line)
    return sets[0].issubset(sets[1]) + sets[1].issubset(sets[0])


def getLineSectionsOverlap(line):
    sets = setArrayOfLine(line)
    return len(sets[0] & sets[1]) > 0


def p1(lines):
    lines = inputFile.read().split()
    return sum(map(getLineSectionsContainOther, lines))


def p2(lines):
    lines = inputFile.read().split()
    return sum(map(getLineSectionsOverlap, lines))

with open("input1.txt", "r") as inputFile:
    lines = inputFile.read().split()
    print(p1(lines))
    print(p2(lines))
