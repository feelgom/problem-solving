from collections import deque

N, M = map(int,input().split())
lines = {i:[] for i in range(1,N+1)}
counts = [0]*(N+1)
for _ in range(M):
    a,b = map(int,input().split())
    lines[a].append(b)
    counts[b]+=1
    
q = deque([i for i in range(1,N+1) if counts[i] == 0])

ans = []    
while q:
    num = q.popleft()
    ans.append(num)
    for i in lines[num]:
        counts[i] -= 1
        if counts[i] == 0:
            q.append(i)
    
print(*ans)
