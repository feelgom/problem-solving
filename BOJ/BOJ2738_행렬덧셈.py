N,M = map(int,input().split())

A = []
B = []
for _ in range(N):
    A.append(list(map(int,input().split())))
for _ in range(N):
    B.append(list(map(int,input().split())))

for i in range(N):
    Ai = A[i]
    Bi = B[i]
    ab = [Ai[j]+Bi[j] for j in range(M)]
    print(*ab)
