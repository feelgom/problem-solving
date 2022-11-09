#%%
import sys
sys.setrecursionlimit(10**9)

def find(x):
    if dp[x] == 0:
        cands = []
        if x % 3 == 0:
            cands.append(find(x//3))
        if x % 2 == 0:
            cands.append(find(x//2))
        cands.append(find(x-1))
        dp[x] = min(cands)+1

    return dp[x]

N = int(input())
if N == 1:
    print(0)
    print(1)
else:
    dp = [0]*(N+1)
    if (N>=2):
        dp[2] = 1
    if (N>=3):
        dp[3] = 1

    print(find(N))
    history = [N]
    while N != 1:
        min_ = N-1
        if N%3 == 0 and dp[min_]>dp[N//3]:
            min_ = N//3       
        if N%2 == 0 and dp[min_]>dp[N//2]:
            min_ = N//2
        history.append(min_)
        N = min_
    print(*history)