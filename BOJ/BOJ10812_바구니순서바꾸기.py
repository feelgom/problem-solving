N, M = map(int,input().split())
lis = list(range(N+1))

for _ in range(M):
    i,j,k = map(int,input().split())
    lis[i:j+1] = lis[k:j+1] + lis[i:k]
    
print(*lis[1:])