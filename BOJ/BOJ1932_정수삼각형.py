#%%
import sys

input = sys.stdin.readline
n = int(input())
tri = []
for _ in range(n):
    tri.append(list(map(int,input().split())))
    
for level in range(1, n):
    
    for i in range(level+1):
        if i == 0:
            tri[level][i] += tri[level-1][0]
        elif i == level:
            tri[level][level] += tri[level-1][level-1]
        else:
            tri[level][i] += max(tri[level-1][i-1], tri[level-1][i])

print(max(tri[n-1]))