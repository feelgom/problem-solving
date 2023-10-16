import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

N, M = map(int, input().split())
roots = [i for i in range(N + 1)]
# 처음에는 모든 노드가 자기 자신을 부모로 가리킴

def find(n):
    if roots[n] != n:
        roots[n] = find(roots[n])
    
    return roots[n]

def union(a,b):
    root_a = find(a)
    root_b = find(b)
    roots[root_a] = root_b

for _ in range(M):
    check, a, b = map(int, input().split())
    if check:
        if find(a) == find(b):
            print("YES")
        else:
            print("NO")
    else:
        union(a,b)