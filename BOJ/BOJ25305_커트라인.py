N,k = map(int,input().split())
lis = list(map(int,input().split()))

lis.sort()
print(lis[-k])