N, M = map(int,input().split())
lis=[0]*(N+1)
for _ in range(M):
    i,j,k = map(int,input().split())
    lis[i:j+1] = [k]*(j-i+1)
    
print(*lis[1:])