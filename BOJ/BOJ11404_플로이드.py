import sys
input = sys.stdin.readline
n = int(input())
m = int(input())

INF = 99999999
lis = [[INF]*(n+1) for _ in range(n+1)]
for i in range(1,n+1):
    lis[i][i] = 0

for _ in range(m):
    start, end, weight = map(int, input().split())
    if weight < lis[start][end]:
        lis[start][end] = weight
    

for i in range(1, n+1):
    for j in range(1, n+1):
        if j == i:
            continue
        for k in range(1, n+1):
            lis[j][k] = min(lis[j][k],  lis[j][i]+lis[i][k])

for i in range(1,n+1):
    for j in range(1,n+1):
        if lis[i][j] == INF:
            lis[i][j] = 0

for i in range(1,n+1):
    print(*lis[i][1:])