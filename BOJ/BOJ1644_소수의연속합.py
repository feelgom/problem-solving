from collections import deque

def prime_list(n = 1000000):
    cands = [True] * n
    LIM = int(n**0.5)
    
    for i in range(2, LIM+1):
        if cands[i] == True:
            for j in range(2*i, n, i):
                cands[j] = False
    
    return [i for i in range(2,n) if cands[i] == True]

def main(N):
    primes = prime_list(N+1)
    temp = deque([])
    ans = 0
    for prime in primes:
        temp.append(prime)
        while sum(temp) > N:
            temp.popleft()
        
        if sum(temp) == N:
            ans += 1
    
    print(ans)

if __name__ == "__main__":
    N = int(input())
    main(N)