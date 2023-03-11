N = int(input())
lis = [] 
for _ in range(N):
    lis.append(list(map(int,input().split())))

ans = []
for x,y in lis:
    rank = 1
    for a,b in lis:
        if x<a and y<b:
            rank+=1
    ans.append(rank)
    
print(*ans)