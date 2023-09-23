import sys
from collections import deque
input = sys.stdin.readline

N=int(input())
tree = {i:[] for i in range(1,N+1)}
for _ in range(N-1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)

parents = [-1]*(N+1)
q = deque([1])

while q:
    node = q.popleft()
    for i in tree[node]:
        parents[i] = node
        tree[i].remove(node)
        q.append(i)
            
for i in range(2, N+1):
    print(parents[i])