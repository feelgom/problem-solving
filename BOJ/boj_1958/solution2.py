strA = input()
strB = input()
strC = input()

dp1 = [[0 for _ in range(len(strB)+1)] for _ in range(len(strA)+1)]

mm = [set([]) for _ in range(100)]
for i in range(1, len(strA)+1):
    for j in range(1, len(strB)+1):
        if strA[i-1] == strB[j-1]:
            dp1[i][j] = dp1[i-1][j-1]+1
            mm[dp1[i][j]].add(strA[i-1])
        else:
            dp1[i][j] = max([dp1[i-1][j], dp1[i][j-1]])

def make_sequence(i,j,seq):
    if i == 0 or j == 0:
        return [seq]
    ans = []
    if dp1[i][j] == dp1[i-1][j]:
        ans = ans + make_sequence(i-1,j,seq)
    elif dp1[i][j] == dp1[i][j-1]:
        ans = ans + make_sequence(i,j-1,seq)
    else:
        ans = make_sequence(i-1,j-1,strA[i-1]+seq)
    
    return ans

length = dp1[-1][-1]
LCSs = make_sequence(len(strA), len(strB), "")
ans = 0
for LCS in LCSs:
    dp2 = [[0 for _ in range(len(strC)+1)] for _ in range(length+1)]
    for i in range(1, length+1):
        for j in range(1, len(strC)+1):
            if LCS[i-1] == strC[j-1]:
                dp2[i][j] = dp2[i-1][j-1]+1
            else:
                dp2[i][j] = max([dp2[i-1][j], dp2[i][j-1]])
    ans = max(ans, dp2[-1][-1])

print(ans)
