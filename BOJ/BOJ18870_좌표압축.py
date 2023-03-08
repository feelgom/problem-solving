import sys
input = sys.stdin.readline

N = int(input())
lis = list(map(int,input().split()))
lis2 = sorted(list(set(lis)))

dic = {}
for i, elem in enumerate(lis2):
    dic[elem] = i
    
ans = []
for num in lis:
    ans.append(dic[num])
    
print(*ans)