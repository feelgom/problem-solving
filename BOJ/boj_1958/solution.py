strA = input()
strB = input()
strC = input()

dp1 = [[[0 for _ in range(len(strC)+1)] for _ in range(len(strB)+1)] for _ in range(len(strA)+1)]

for i in range(1, len(strA)+1):
    for j in range(1, len(strB)+1):
        for k in range(1, len(strC)+1):
            if strA[i-1] == strB[j-1] == strC[k-1]:
                dp1[i][j][k] = dp1[i-1][j-1][k-1]+1
            else:
                dp1[i][j][k] = max([dp1[i-1][j][k], dp1[i][j-1][k], dp1[i][j][k-1]])


print(dp1[-1][-1][-1])
