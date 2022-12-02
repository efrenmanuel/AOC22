
def pa(part):
    with open("input1.txt", "r") as inputFile:
        points = 0
        for line in inputFile:
            gameRound = line.split()

            # A|X = Rock     = 0
            # B|Y = Paper    = 1
            # C|Z = Scissors = 2

            #For part 2
            #X = Win      = -1
            #Y = Draw     =  0
            #Z = Lose     =  1
            elf = ord(gameRound[0]) - 65
            you = ord(gameRound[1]) - 88 if part==1 else (ord(gameRound[1]) - 89 + elf) % 3
            
            points += (1 - elf + you) % 3 * 3 + you + 1
        return (points)

print(pa(1))
print(pa(2))