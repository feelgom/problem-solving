N = int(input())
lis = []
for _ in range(N):
    lis.append(input())
    
lis = list(set(lis))

lis = sorted(lis, key=lambda x:(len(x), x))
for elem in lis:
    print(elem)
