import sys
import heapq

input = sys.stdin.readline
V = int(input())


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


root = [i for i in range(V + 1)]
planets = []
for i in range(V):
    planets.append(list(map(int, input().split())) + [i])

lines = []
for i in range(3):
    planets.sort(key=lambda x: x[i])
    for j in range(V - 1):
        edge = (
            abs(planets[j][i] - planets[j + 1][i]),
            planets[j][3],
            planets[j + 1][3],
        )
        lines.append(edge)

lines.sort()

ans = 0
root = [i for i in range(V + 1)]
for weight, start, end in lines:
    if find(start) != find(end):
        union(start, end)
        ans += weight

print(ans)
