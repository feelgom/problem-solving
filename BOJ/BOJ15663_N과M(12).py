#%%
from itertools import combinations_with_replacement

N, M = map(int,input().split())
nums = list(set(map(int,input().split())))
nums.sort()

lis = list(combinations_with_replacement(nums,M))
for elem in lis:
    print(*elem)