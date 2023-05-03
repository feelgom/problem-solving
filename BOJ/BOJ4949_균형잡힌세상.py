ans = []
while True:
    string = input()
    if string == ".":
        break
    
    stack = []
    for char in string:
        if char == "(" or char == "[":
            stack.append(char)
        elif char == ")":
            if not stack or stack.pop() != "(":
                #print("no")
                ans.append(string + " no")
                break
        elif char == "]":
            if not stack or stack.pop() != "[":
                #print("no")
                ans.append(string + " no")
                break
    else:
        if not stack:
            #print("yes")
            ans.append(string + " yes")
        else:
            #print("no")
            ans.append(string + " no")

for elem in ans:
    print(elem)
