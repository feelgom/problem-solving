T = int(input())

for _ in range(T):
    R, string = input().split()
    R = int(R)
    
    ans = ""
    for char in string:
        ans += char*R
    
    print(ans)