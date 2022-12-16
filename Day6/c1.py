def p1(marker_len):
    with open("input1.txt", "r") as inputFile:
        line = inputFile.read()
        for i in range(0,len(line)-marker_len):
            if len(set(line[i:i+marker_len])) == marker_len:
                return i+marker_len

print(p1(4))
print(p1(14))