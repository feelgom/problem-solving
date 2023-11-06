N=int(input())
ans = 0
for _ in range(N):
    a,b,c = map(int,input().split())
    if a+b+c >= 2:
        ans += 1
        
print(ans)