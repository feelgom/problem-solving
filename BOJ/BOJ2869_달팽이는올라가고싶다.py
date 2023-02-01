from math import ceil
A,B,V = map(int,input().split())
ans = ceil((V-A)/(A-B)) + 1
print(ans)