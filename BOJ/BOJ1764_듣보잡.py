N,M = map(int,input().split())
dic = {}
lis = []
for _ in range(N):
    dic[input()] = True
for _ in range(M):
    name = input()
    if name in dic:
        lis.append(name)
        
lis.sort()
print(len(lis))
for elem in lis:
    print(elem)