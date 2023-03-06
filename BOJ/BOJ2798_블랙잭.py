from itertools import combinations

N, M = map(int,input().split())
lis = list(map(int,input().split()))
combis = combinations(lis, 3)

max_sum = 0
for elem in combis:
    if sum(elem) > max_sum and sum(elem) <= M:
        max_sum = sum(elem)
        
print(max_sum)
