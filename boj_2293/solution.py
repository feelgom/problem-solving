N,K = map(int,input().split())
coins = [int(input()) for _ in range(N)]
coins.sort(reverse=True)

dp = [0]*(K+1)
dp[0] = 1
for coin in coins:
    for i in range(K+1):
        if i+coin <= K:
            dp[i+coin] += dp[i]

print(dp[K])