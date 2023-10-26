N = int(input())

A = [0]+list(map(int,input().split()))+[10000]
length = [0]*(N+2)

for i in range(N):
    for j in range(N-i+1,N+2):     
        if A[j] > A[N-i]:
            if length[N-i] <= length[j]:
                length[N-i] = length[j]+1
                
print(max(length))                