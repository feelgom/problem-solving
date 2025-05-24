string = input()
separator = input()
if len(separator) == 0:
    separator = input()

while True:
    q = []
    for c in string:
        q.append(c)
        if len(q) >= len(separator) and ''.join(q[-len(separator):]) == separator:
            for _ in range(len(separator)):
                q.pop()
    
    if len(q) == 0:
        print('FRULA')
        break
    
    string2 = ''.join(q)
    if string2 == string:
        print(string)
        break
    string = string2
    