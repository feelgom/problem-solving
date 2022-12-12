import sys
from math import inf
import heapq
input = sys.stdin.readline

N,M,X = map(int,input().split())

distance1 = [[inf]*(N+1) for _ in range(N+1)]
distance2 = [[inf]*(N+1) for _ in range(N+1)]
for _ in range(M):
    start, end, weight = map(int, input().split())
    distance1[end][start] = weight
    distance2[start][end] = weight

shortest1 = [inf]*(N+1)
shortest1[X] = 0
visit = []
heapq.heappush(visit,(0,X))
while visit:
    weight, node = heapq.heappop(visit)
    if shortest1[node] < weight:
        continue
    for start, val in enumerate(distance1[node]):
        if weight + val < shortest1[start]:
            shortest1[start] = weight + val
            heapq.heappush(visit, (shortest1[start], start))
        
shortest2 = [inf]*(N+1)
shortest2[X] = 0
visit = []
heapq.heappush(visit,(0,X))
while visit:
    weight, node = heapq.heappop(visit)
    if shortest2[node] < weight:
        continue
    for start, val in enumerate(distance2[node]):
        if weight + val < shortest2[start]:
            shortest2[start] = weight + val
            heapq.heappush(visit, (shortest2[start], start))
        
answer = [x+y for x,y in zip(shortest1, shortest2)]
print(max(answer[1:]))
    
