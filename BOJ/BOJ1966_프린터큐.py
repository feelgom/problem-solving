from collections import deque
T = int(input())
for _ in range(T):
    N,M = map(int,input().split())
    priority = deque(map(int,input().split()))
    while M >= 0:
        M -= 1
        if priority[0] == max(priority):
            priority.popleft()
        else:
            priority.append(priority.popleft())
            if M == -1:
                M = len(priority) - 1
    
    print(N - len(priority))