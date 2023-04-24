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
                print("no")
                break
        elif char == "]":
            if not stack or stack.pop() != "[":
                print("no")
    else:
        if not stack:
            print("yes")
        else:
            print("no")