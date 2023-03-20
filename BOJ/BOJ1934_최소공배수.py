T = int(input())
for _ in range(T):
    a, b = map(int,input().split())
    big = max(a,b)
    small = min(a,b)
    
    while True:
        remainder = big % small
        if remainder == 0:
            GCF = small
            break
        big = small
        small = remainder
        
    print(int(a*b/GCF))