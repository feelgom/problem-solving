lis = []
for _ in range(5):
    lis.append(int(input()))
    
lis.sort()
print(int(sum(lis)/len(lis)))
print(lis[2])