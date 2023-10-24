import sys
import heapq

input = sys.stdin.readline
V = int(input())


def add_node(node):
    visited[node] = True
    for elem in lines[node]:
        heapq.heappush(q, elem)


def distance(star1, star2):
    return ((star1[0] - star2[0]) ** 2 + (star1[1] - star2[1]) ** 2) ** 0.5


stars = []
for _ in range(V):
    stars.append(list(map(float, input().split())))

lines = [[] for _ in range(V)]
for i in range(V):
    for j in range(i + 1, V):
        lines[i].append((distance(stars[i], stars[j]), j))
        lines[j].append((distance(stars[i], stars[j]), i))

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
print(round(ans, 2))
