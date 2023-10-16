from itertools import combinations

L,C=map(int,input().split())
alpha=input().split()
alpha.sort()

combis = list(combinations(alpha,L))
for combi in combis:
    count=0
    for i in combi:
        if i in 'aeiou':
            count+=1
    if count>=1 and count<=L-2:
        print(''.join(combi))

