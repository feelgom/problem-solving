while 1:
    string = input()
    if string == '*':
        break
    PASS = True
    length = len(string)
    for l in range(1, length):
        if PASS == False:
            break
        dic = {}
        for i in range(length-l):
            temp = string[i]+string[i+l]
            if temp not in dic:
                dic[temp] = 1
            else:
                PASS = False
                break
    if PASS:
        print(string, "is surprising.")
    else:
        print(string, "is NOT surprising.")