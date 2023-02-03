T = int(input())
for _ in range(T):
    k = int(input())
    n = int(input())
    prev = list(range(1, n+1))
    for i in range(k):
        this = [sum(prev[:j]) for j in range(1,n+1)]
        prev = this
    
    print(this[n-1])