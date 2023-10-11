# Greedy로는 안풀리는 2차원 dp 문제

N, K = map(int, input().split())
dp = [[0] * (K + 1) for _ in range(N + 1)]
# dp[i][j]는 i번째 물건을 고려했을 때 용량이 j인 가방을 채울 수 있는 value를 나타낸다.

for i in range(1, N + 1):
    W, V = map(int, input().split())
    for j in range(K + 1):
        if W > j:
            dp[i][j] = dp[i - 1][j]
        else:
            cand1 = dp[i - 1][j]
            cand2 = dp[i - 1][j - W] + V
            dp[i][j] = max(cand1, cand2)

print(dp[N][K])
