N,M = map(int,input().split())

lis = list(range(N+1))
for _ in range(M):
    i, j = map(int, input().split())
    lis[i], lis[j] = lis[j], lis[i]
    
print(*lis[1:])