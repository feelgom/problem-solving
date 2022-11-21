#%%
from itertools import combinations

N, M = map(int,input().split())

lis = list(combinations(range(1,N+1),M))
for elem in lis:
    print(*elem)