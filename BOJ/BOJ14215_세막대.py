lis = list(map(int, input().split()))
lis.sort()
lis[2] = min(lis[0]+lis[1] - 1, lis[2])
print(sum(lis))
