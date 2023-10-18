import sys

input = sys.stdin.readline

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
            
    weight_sum = 0
    lines = []
    for _ in range(E):
        a, b, c = map(int, input().split())
        lines.append((c, a, b))
        weight_sum += c

    lines.sort()

    ans = 0
    root = [i for i in range(V + 1)]
    for weight, start, end in lines:
        if find(start) != find(end):
            union(start, end)
            ans += weight

    print(weight_sum - ans)

while True:
    V, E = map(int, input().split())
    if V == 0 and E == 0:
        break
    kruscal()