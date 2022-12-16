import sys
import heapq
input = sys.stdin.readline

N = int(input())
dic = {}
max_deadline = 0
for _ in range(N):
    deadline, point = map(int,input().split())
    if deadline not in dic:
        dic[deadline] = []
    dic[deadline].append(point)
    if deadline > max_deadline:
        max_deadline = deadline

heap = []
score = 0
for i in range(max_deadline):
    dead = max_deadline - i
    if dead in dic:
        for elem in dic[dead]:
            heapq.heappush(heap,[-elem,elem])
    if heap:
        pick = heapq.heappop(heap)
        score +=pick[1]
print(score)