#%%
N = int(input())

lis = list(map(int, input().split()))
lis2 = []
for i, a in enumerate(lis):
    lis2.append([a, i])

lis2.sort()
lis3 = [0]*N
for i, item in enumerate(lis2):
    lis3[item[1]]= i

print(*lis3)