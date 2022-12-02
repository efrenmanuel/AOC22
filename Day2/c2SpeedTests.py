

def p2():
    with open("input1.txt", "r") as inputFile:
        points = 0
        for line in inputFile:
            #['A','X']
            gameRound = line.split()

            #A = Rock     =  0
            #B = Paper    =  1
            #C = Scissors =  2
            elf = sum(ord(gameRound[0]), -65)
            
            #X = Win      = -1
            #Y = Draw     =  0
            #Z = Lose     =  1
            you = (ord(gameRound[1]) - 89 + elf) % 3

            #print("{elf},{letter},{you}".format(elf=gameRound[0],letter=gameRound[1], you=chr(you+65)))
            # print((2-elf+you-1)%3) # 0 if lost, 1 if draw, 2 if won
            points += (1 - elf + you) % 3 * 3 + you + 1
        return points

print(p2())