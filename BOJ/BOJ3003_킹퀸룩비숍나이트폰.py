full = [1,1,2,2,2,8]

now = list(map(int,input().split()))
ans = []
for i in range(len(now)):
    diff =  full[i] - now[i]
    ans.append(diff)
print(*ans)