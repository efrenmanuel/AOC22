
def p1():
    with open("input1.txt", "r") as inputFile:
        points = 0
        for line in inputFile.readlines():
            gameRound = line.split()

            # A|X = Rock     = 0
            # B|Y = Paper    = 1
            # C|Z = Scissors = 2
            elf = ord(gameRound[0]) - 65
            you = ord(gameRound[1]) - 88
            
            #print("{elf},{you}".format(elf=elf, you=you))
            # print((2-elf+you-1)%3) # 0 if lost, 1 if draw, 2 if won
            points += (1 - elf + you) % 3 * 3 + you + 1
        return (points)

print(p1())