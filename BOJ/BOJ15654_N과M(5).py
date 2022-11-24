#%%
from itertools import permutations

N, M = map(int,input().split())
nums = list(map(int,input().split()))
nums.sort()

lis = list(permutations(nums,M))
for elem in lis:
    print(*elem)