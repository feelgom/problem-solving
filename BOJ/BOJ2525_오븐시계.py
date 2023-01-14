h,m = map(int,input().split())
c = int(input())

total = 60*h + m + c

H = total//60%24
M = total%60

print(H, M)