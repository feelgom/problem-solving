from collections import deque
N,M = map(int,input().split())
cand = list(map(int,input().split()))

ans = 0
for i in range(M):
    elem = cand[i]
    temp = min(elem-1, N-elem+1)
    ans += temp
    if i != M-1:
        cand[i+1:] = [(x-elem)%N for x in cand[i+1:]]
    N-=1
print(ans)
    