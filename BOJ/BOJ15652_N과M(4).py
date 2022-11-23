#%%
from itertools import combinations_with_replacement

N, M = map(int,input().split())

lis = list(combinations_with_replacement(range(1,N+1),M))
for elem in lis:
    print(*elem)