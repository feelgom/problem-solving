T = int(input())

for _ in range(T):
    ox = input()
    ans = 0
    cont = 0
    for char in ox:
        if char == "O":
            cont+=1
            ans+= cont
        else:
            cont = 0
    print(ans)
    