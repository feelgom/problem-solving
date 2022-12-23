#%%
N = int(input())

lis = list(map(int, input().split()))
lis2 = []
for i, a in enumerate(lis):
    lis2.append([a, i])

lis2.sort(reverse=True)
lis3 = []
for _, i in lis2:
    lis3.append(i)

print(*lis3)