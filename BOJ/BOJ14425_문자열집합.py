import sys
input = sys.stdin.readline

N,M = map(int,input().split())
dic = {}
for _ in range(N):
    dic[input()] = 1

ans = 0
for _ in range(M):
    if input() in dic:
        ans +=1
        
print(ans)