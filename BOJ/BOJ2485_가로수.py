def GCF(a, b):
    while b:
        a, b = b, a%b
    return a

N = int(input())
lis = []
for _ in range(N):
    lis.append(int(input()))

lis2 = []
for i in range(N-1):
    lis2.append(lis[i+1] - lis[i])

gcf = lis2[0]
for elem in lis2:
    gcf = GCF(gcf, elem)
    
ans = 0
for elem in lis2:
    ans += elem//gcf - 1

print(ans)