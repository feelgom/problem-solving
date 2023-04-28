import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
queue = deque([])
for _ in range(N):
    string = input().split()
    if string[0] == "push_front":
        queue.appendleft(string[1])
    elif string[0] == "push_back":
        queue.append(string[1])
    elif string[0] == "pop_front":
        if len(queue)>0:
            print(queue.popleft())
        else:
            print(-1)
    elif string[0] == "pop_back":
        if len(queue)>0:
            print(queue.pop())
        else:
            print(-1)
    elif string[0] == "size":
        print(len(queue))
    elif string[0] == "empty":
        if len(queue) == 0:
            print(1)
        else:
            print(0)
    elif string[0] == "front":
        if len(queue)>0:
            print(queue[0])
        else:
            print(-1)
    elif string[0] == "back":
        if len(queue)>0:
            print(queue[-1])
        else:
            print(-1)
    