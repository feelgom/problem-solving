import sys
import heapq

input = sys.stdin.readline
V, E = map(int, input().split())


# 1. Kruscal's algorithm
def kruscal():
    def find(a):
        if root[a] != a:
            root[a] = find(root[a])

        return root[a]

    def union(a, b):
        root_a = find(a)
        root_b = find(b)

        if root_a < root_b:
            root[root_b] = root_a
        else:
            root[root_a] = root_b

    lines = []
    for _ in range(E):
        a, b, c = map(int, input().split())
        lines.append((c, a, b))

    lines.sort()

    ans = 0
    root = [i for i in range(V + 1)]
    for weight, start, end in lines:
        if find(start) != find(end):
            union(start, end)
            ans += weight

    print(ans)


# 2. Prim's algorithm
def prim():
    def add_node(node):
        visited[node] = True
        for elem in lines[node]:
            heapq.heappush(q, elem)

    lines = {}
    for _ in range(E):
        a, b, c = map(int, input().split())
        if a not in lines:
            lines[a] = []
        if b not in lines:
            lines[b] = []
        lines[a].append((c, b))
        lines[b].append((c, a))

    ans = 0
    q = []
    visited = [False] * (V + 1)
    add_node(1)
    count = 1
    while q:
        weight, end = heapq.heappop(q)
        if not visited[end]:
            ans += weight
            add_node(end)
            count += 1

        if count == V:
            break
    print(ans)


# kruscal()
prim()
