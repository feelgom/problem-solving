def solution(N, coins, M):
    dp = [[0] * (M + 1) for _ in range(N + 1)]
    for i in range(N+1):
        dp[i][0] = 1

    for i in range(1, N+1):
        coin = coins[-i]
        for j in range(coin,M+1):
            dp[i][j] = dp[i-1][j] + dp[i][j-coin]
    
    print(dp[N][M])

T=int(input())
for _ in range(T):
    N=int(input())
    coins = list(map(int,input().split()))
    M = int(input())
    solution(N, coins, M)
