#%%
import copy
N, T = map(int,input().split())

A = []
for _ in range(N):
    A.append(list(map(int,input().split())))

temp = copy.deepcopy(A)
for _ in range(T-1):
    temp2 = [[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            for k in range(N):
                temp2[i][j] += temp[i][k] * A[k][j]
            temp2[i][j] %= 1000
    temp = temp2
    
    
for i in range(N):    
    print(*temp[i])
    