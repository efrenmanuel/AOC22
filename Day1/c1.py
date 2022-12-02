def p1():
    with open("input1.txt", "r") as inputFile:
        counter=1
        maxCookies=0
        maxElf=1
        currCookies=0

        for line in inputFile:
            if line == "\n":
                if currCookies>maxCookies:
                    maxCookies=currCookies
                    maxElf=counter
                currCookies=0
                counter+=1
            else:
                currCookies+=int(line)
        if currCookies>maxCookies:
            maxCookies=currCookies
            maxElf=counter
        print((maxElf,maxCookies))

p1()