N,M = map(int,input().split())
lis1 = input().split()
dict1 = {}
for elem in lis1:
    dict1[elem] = True

lis2 = input().split()
intersection_count = 0
for elem in lis2:
    if elem in dict1:
        intersection_count +=1
        
ans = N + M - intersection_count*2
print(ans)