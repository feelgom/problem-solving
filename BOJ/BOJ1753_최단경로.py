#%%
import sys
import heapq
from math import inf
input = sys.stdin.readline

V,E = map(int,input().split())
start = int(input())

world = { i: {} for i in range(V)}
for _ in range(E):
    begin, end, weight = map(int,input().split())
    if end-1 not in world[begin-1]:
        world[begin-1][end-1] = weight
    else: 
        if world[begin-1] and world[begin-1][end-1] > weight:
            world[begin-1][end-1] = weight

visit = []
dis = [inf]*V
dis[start-1] = 0
heapq.heappush(visit, (0, start-1))

while visit:
    weight, node = heapq.heappop(visit)
    if dis[node] < weight:
        continue
    for end, val in world[node].items():
        if weight + val  < dis[end]:
            dis[end] = weight+val
            heapq.heappush(visit, (dis[end], end))
        
for elem in dis:
    if elem == inf:
        print("INF")
    else:
        print(elem)