crates=[]
instructions=[]

def parseInstruction(line):
    return [int(item) for item in line.split()[1::2]]

def performInstruction(instruction):
    global crates
    if len(instruction)>0:
        for i in range(0,instruction[0]):
            crates[instruction[2]-1].append(crates[instruction[1]-1].pop())

def performInstructionv2(instruction):
    global crates
    if len(instruction)>0:
        crates[instruction[2]-1].extend(crates[instruction[1]-1][-instruction[0]:])
        del crates[instruction[1]-1][-instruction[0]:]
        
        

def loadInput():
    with open("input1.txt", "r") as inputFile:
        lines = inputFile.read().split('\n')
        index, size = next(((i,int(s.split()[-1])) for i, s in enumerate(lines) if s.startswith(' 1')), None)
        print(index)
        parsedLine=[[line[x*4+1] for x in range(0,size)] for line in lines[index-1::-1]]
        global crates
        crates=[[item for item in line if item.strip()!=""] for line in zip(*parsedLine)]
        global instructions
        instructions=list(map(parseInstruction, lines[index+2:]))
        
def p1():
    #loadInput()
    global instructions
    #map(performInstruction, instructions)
    for instruction in instructions:
        performInstruction(instruction)
    global crates
    return "".join([column[-1] for column in crates])
        

def p2():
    #loadInput()
    global instructions
    #map(performInstruction, instructions)
    for instruction in instructions:
        performInstructionv2(instruction)
    global crates
    return "".join([column[-1] for column in crates if len(column)>0])
        



loadInput()      
print(p1())
loadInput()    
print(p2())
