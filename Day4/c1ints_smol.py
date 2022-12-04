def getLineSectionsContainOther(line):
    arr = [[int(s) for s in sections.split("-")]
           for sections in line.split(",")]
    return ((arr[0][0] <= arr[1][0] and arr[0][1] >= arr[1][1]) or
            (arr[1][0] <= arr[0][0] and arr[1][1] >= arr[0][1]))


def getLineSectionsOverlap(line):
    arr = [[int(s) for s in sections.split("-")]
           for sections in line.split(",")]
    return (arr[1][0] <= arr[0][0] <= arr[1][1] or
            arr[1][0] <= arr[0][1] <= arr[1][1] or
            arr[0][0] <= arr[1][0] <= arr[0][1] or
            arr[0][0] <= arr[1][1] <= arr[0][1])


def p1():
    with open("input1.txt", "r") as inputFile:
        lines = inputFile.read().split()
        return sum(map(getLineSectionsContainOther, lines))


def p2():
    with open("input1.txt", "r") as inputFile:
        lines = inputFile.read().split()
        return sum(map(getLineSectionsOverlap, lines))


print(p1())
print(p2())
