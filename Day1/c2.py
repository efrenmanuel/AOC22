def p2():
    elves=[]
    with open("input1.txt", "r") as inputFile:
        currCookies=0

        for line in inputFile:
            if line == "\n":
                elves.append(currCookies)
                currCookies=0
            else:
                currCookies+=int(line)
        elves.sort()

        print(sum(elves[-3::]),elves[-3::])

p2()