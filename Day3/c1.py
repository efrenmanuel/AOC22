from functools import reduce

def priority(inputSets):
    

    repeated=ord(reduce(lambda a,b: a & b, inputSets).pop())
    val = repeated-96 if repeated > 96 else repeated-38
    return val

def makeSetArrayOfLine(line):
    return [set(line[:len(line)//2]), set(line[len(line)//2:])]

def getLinePriority(line):
    return priority(makeSetArrayOfLine(line))

def p1():
    with open("input1.txt", "r") as inputFile:
        lines=inputFile.readlines()
        return sum(map(getLinePriority, lines))

def makeSetArrayFromArray(lines, linesPerSet):
    for i in range(0, len(lines), linesPerSet):
        yield([set(line) for line in lines[i:i+linesPerSet]])

def p2():
    with open("input1.txt", "r") as inputFile:
        lines=inputFile.read().split()
        return sum(map(priority, makeSetArrayFromArray(lines,3)))  
            

print(p1())
print(p2())
