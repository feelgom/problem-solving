# 바이러스

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

N = int(input())
L = int(input())

graph = [[] for _ in range(N+1)]
for i in range(L):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

visit = [False for _ in range(N+1)]
def DFS(v):
    if visit[v] == True:
        return
    else:
        visit[v] = True
        # print(v)
        for u in graph[v]:
            DFS(u)

DFS(1)
print(sum(visit)-1)