from heapq import heappop, heappush
import sys

heap = []

N = int(input())

for _ in range(N):
    num = int(sys.stdin.readline().strip())
    if num == 0:
        if heap:
            print(heappop(heap))
        else:
            print(0)
    else:
        heappush(heap,num)
            
 
        