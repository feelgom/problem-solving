import sys
input = sys.stdin.readline

N = int(input().strip())
dic = []
ans = 0
for _ in range(N):
    str = input().strip()
    if str == "ENTER":
        ans += len(set(dic))
        dic = []
    else:
        dic.append(str)
        
ans += len(set(dic))
print(ans)