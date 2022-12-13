N = int(input())


dp = [0,1]

for _ in range(N-1):
    temp = dp.pop(0)
    new = (temp+dp[0])%1000000007
    dp.append(new)

print(dp[1])