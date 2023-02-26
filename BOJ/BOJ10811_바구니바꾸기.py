N,M = map(int,input().split())

lis = list(range(N+1))
for _ in range(M):
    i, j = map(int, input().split())
    lis[i:j+1] = lis[i:j+1][::-1]
    
print(*lis[1:])
