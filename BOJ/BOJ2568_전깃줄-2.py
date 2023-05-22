import sys
input = sys.stdin.readline

N=int(input())
lines=[]
for _ in range(N):
    line=list(map(int,input().split()))
    lines.append(line)

lines.sort(key=lambda x:x[0])

# LIS 알고리즘 구현에 두 가지 방법이 있는데 BOJ2565_전깃줄 문제에서는 O(n^2) 방법을 사용했다.
# 하지만 이 문제에서는 N의 최댓값이 100000이므로 n^2의 시간복잡도를 가진 알고리즘은 시간초과가 난다.
# 따라서 이 문제에서는 O(nlogn)의 시간복잡도를 가지는 LIS 알고리즘을 사용한다.

# dp = {i:[i] for i in range(N)}
# for i in range(1,N):
#     for j in range(i):
#         if lines[i][1]>lines[j][1]:
#             if len(dp[i])<len(dp[j])+1:
#                 dp[i]=dp[j]+[i]

LIS = []
indexes = []
for i in range(N):
    if not LIS or lines[i][1]>LIS[-1]:
        LIS.append(lines[i][1])
        indexes.append(len(LIS))
    else:
        start,end=0,len(LIS)-1
        while start < end:
            mid = (start+end)//2
            if LIS[mid] < lines[i][1]:
                start = mid+1
            else:
                end = mid
        LIS[end]=lines[i][1]
        indexes.append(end+1)

# print([elem[1] for elem in lines])
# print(LIS)
# print(indexes)

lis_length = len(LIS)
final = []
for i in range(N-1,-1,-1):
    if indexes[i] == lis_length:
        final.append(lines[i][1])
        lis_length-=1

# print(final)
print(N-len(final))
ans = []
for i in range(N):
    if lines[i][1] not in final:
        ans.append(lines[i][0])
        
ans.sort()
for elem in ans:
    print(elem)