import sys
import math
input = sys.stdin.readline

R,G,B = 0,0,0
N=int(input())
scores = []
for _ in range(N):
    scores.append(list(map(int,input().split())))

ans = math.inf
R,G,B = 0,0,0
for i in range(N):
    r,g,b = scores[i]
    if i == 0:
        R,G,B = math.inf,g,b
    else:
        R,G,B = min(G,B)+r, min(R,B)+g, min(R,G)+b

ans = min(ans, R)

R,G,B = 0,0,0
for i in range(N):
    r,g,b = scores[i]
    if i == 0:
        R,G,B = r,math.inf,b
    else: 
        R,G,B = min(G,B)+r, min(R,B)+g, min(R,G)+b

ans = min(ans, G)


R,G,B = 0,0,0
for i in range(N):
    r,g,b = scores[i]
    if i == 0:
        R,G,B = r,g,math.inf
    else:
        R,G,B = min(G,B)+r, min(R,B)+g, min(R,G)+b

ans = min(ans, B)
print(ans)
