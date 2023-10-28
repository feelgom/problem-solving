N = int(input())

A = [0] + list(map(int,input().split()))+[10000]
length = [0]*(N+2)

for i in range(N+1):
    for j in range(i):
        if A[j] < A[i]:
            if length[i] <= length[j]:
                length[i] = length[j]+1
                
print(max(length))