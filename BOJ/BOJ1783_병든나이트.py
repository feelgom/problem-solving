N,M = map(int,input().split())

if N >= 3:
    if M >= 7:
        print(M-2)
    elif M >= 4:
        print(4)
    else:
        print(M)
elif N == 2:
    an = (M+1)//2
    print(min(an,4))
elif N == 1:
    print(1)
