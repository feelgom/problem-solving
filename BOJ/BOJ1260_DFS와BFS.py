from collections import deque
import sys
sys.setrecursionlimit(10**6)

input = sys.stdin.readline

N, M, v = map(int, input().split())

# 그래프화
graph = [ [] for _ in range(N+1) ]
for i in range(M):
    a, b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

for line in graph:
    line.sort()

def DFS(graph, visit, v):
    if visit[v] == True:
        return
    else:
        visit[v] = True
        print(v,end = ' ')
        for node in graph[v]:
            DFS(graph,visit,node)


def BFS(graph, visit, v):
    if visit[v] == True:
        return
    else:
        visit[v] = True
        print(v,end = ' ')
        for u in graph[v]:
            q.append(u)
            
        while q:
            u = q.popleft()
            BFS(graph, visit, u)

    

    
visit = [False for _ in range(N+1)]
DFS(graph,visit,v)
print("")
q = deque()
visit = [False for _ in range(N+1)]
BFS(graph,visit,v)