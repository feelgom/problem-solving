import sys

input = sys.stdin.readline
V = int(input())
E = int(input())

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