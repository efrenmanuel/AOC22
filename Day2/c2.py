def p2():
    with open("input1.txt", "r") as inputFile:
        points=0
        for line in inputFile:
            round=line.replace("\n","").split(" ")
            #A|X = Rock     = 0
            #B|Y = Paper    = 1
            #C|Z = Scissors = 2
            elf=ord(round[0])-65
            you=(ord(round[1])-89+elf)%3
            
            print("{elf},{letter},{you}".format(elf=round[0],letter=round[1], you=chr(you+65)))
            print((2-elf+you-1)%3) # 0 if lost, 1 if draw, 2 if won
            points+=(1-elf+you)%3*3+you+1
        print(points)

p2()