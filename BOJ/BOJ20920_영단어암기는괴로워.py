import sys
input=sys.stdin.readline
N,M=map(int,input().split())
lis = {}
for _ in range(N):
    word = input().strip()
    if len(word) < M:
        continue
    if word in lis:
        lis[word] += 1
    else:
        lis[word] = 1

for word in sorted(lis, key=lambda x: (-lis[x], -len(x), x)):
    print(word)