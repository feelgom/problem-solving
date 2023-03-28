def is_prime(n):
    if n <2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

T = int(input())

for _ in range(T):
    N = int(input())
    for i in range(N, 10000000000):
        if is_prime(i):
            print(i)
            break
