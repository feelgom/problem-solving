import sys
input = sys.stdin.readline
# 소수 판별 함수
def is_prime_number(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

T = int(input())
# 골드바흐 파티션 구하기

primes = [False]
for _ in range(T):
    n = int(input())
    start = len(primes)
    for i in range(start, n+1):
        primes.append(is_prime_number(i))
    
    count = 0
    for i in range(n//2+1):
        if primes[i] and primes[n-i]:
            count+=1
    
    print(count)