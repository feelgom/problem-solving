from collections import deque

N,K = map(int,input().split())
queue = deque(range(1,N+1))
ans = "<"
count = 0
while queue:
    count += 1
    a = queue.popleft()
    if count % K == 0:
        ans += str(a)+", "
    else:
        queue.append(a)

ans = ans[:-2]+">"
print(ans)
