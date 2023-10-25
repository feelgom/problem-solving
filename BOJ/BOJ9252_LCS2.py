strA = input()
strB = input()

dp = [[0 for _ in range(len(strB)+1)] for _ in range(len(strA)+1)]

for i in range(1, len(strA)+1):
    for j in range(1, len(strB)+1):
        if strA[i-1] == strB[j-1]:
            dp[i][j] = dp[i-1][j-1]+1
        else:
            dp[i][j] = max([dp[i-1][j], dp[i][j-1]])

ans = ""
i = -1
j = -1
while True:
    if i == -len(strA)-1 or j == -len(strB)-1:
        break
    if dp[i][j] == dp[i-1][j]:
        i -= 1
    elif dp[i][j] == dp[i][j-1]:
        j -= 1
    else:
        ans = strA[i] + ans
        i -= 1
        j -= 1
        
print(dp[-1][-1])
print(ans)
