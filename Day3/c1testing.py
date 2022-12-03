from functools import reduce

def priority(inputSets):
    

    repeated=ord(reduce(lambda a, b: a & b, inputSets).pop())
    #val = repeated-96 if repeated > 96 else repeated-38
    val = (repeated-38) % 58
    return val

def makeSetArrayOfLine(line):
    return [set(line[:len(line)//2]), set(line[len(line)//2:])]

def getLinePriority(line):
    return priority(makeSetArrayOfLine(line))

def p1(inputLines):
    
    return sum(map(getLinePriority, inputLines))

def makeSetArrayFromArray(lines, linesPerSet):
    for i in range(0, len(lines), linesPerSet):
        yield([set(line) for line in lines[i:i +  linesPerSet]])

def p2(inputLines):
    return sum(map(priority, makeSetArrayFromArray(inputLines, 3)))  
            
with open("input1.txt", "r") as inputFile:
    lines=inputFile.read().split()
    print(p1(lines))
    print(p2(lines))
