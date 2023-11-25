N = int(input())

for _ in range(N):
    stack = 0
    str = input()
    for elem in str:
        if elem == "(":
            stack += 1
        elif elem == ")":
            stack -= 1
            if stack < 0:
                break

    if stack == 0:
        print("YES")
    else:
        print("NO")
    