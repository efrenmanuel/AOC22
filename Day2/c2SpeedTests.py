#A = Rock     =  0
#B = Paper    =  1
#C = Scissors =  2

#X = Win      = -1
#Y = Draw     =  0
#Z = Lose     =  1

import time
from functools import reduce

def p2():
    with open("input1.txt", "r") as inputFile:
        points = 0
        for line in inputFile:
            gameRound = line.split()

            elf = ord(gameRound[0]) - 65
            you = (ord(gameRound[1]) - 89 + elf) % 3

            #print("{elf},{letter},{you}".format(elf=gameRound[0],letter=gameRound[1], you=chr(you+65)))
            # print((2-elf+you-1)%3) # 0 if lost, 1 if draw, 2 if won
            points += (1 - elf + you) % 3 * 3 + you + 1
        return points

def calc(gameRound):
    elf = (ord(gameRound[0]) - 65)
    you = (ord(gameRound[1]) - 89 + elf) % 3

    return  (1 - elf + you) % 3 * 3 + you + 1

def p2new():
    with open("input1.txt", "r") as inputFile:
        points = 0
        return reduce(lambda c, line:c+calc(line.split()),inputFile,0)
        return sum(map(calc,inputFile))
        return functools.reduce()

print(p2())
print(p2new())

start_time = time.time()
for i in range(0,1000): p2()
print("--- %s seconds ---" % ((time.time() - start_time)/1000))

start_time = time.time()
for i in range(0,1000): p2new()
print("--- %s seconds ---" % ((time.time() - start_time)/1000))
