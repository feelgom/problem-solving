T = int(input())

for _ in range(T):
    lis = list(map(int,input().split()))
    lis = lis[1:]
    avg = sum(lis)/len(lis)
    
    over_lis = [i for i in lis if i>avg]
    percent = len(over_lis) / len(lis)
    print(format(percent, ".3%"))