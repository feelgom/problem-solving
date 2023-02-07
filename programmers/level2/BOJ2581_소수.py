import math
def is_prime_number(x):
    if x <= 1:
        return False
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False 
    return True

M = int(input())
N = int(input())
prime_min = 0
prime_sum = 0
for i in range(M,N+1):
    if is_prime_number(i):
        prime_sum += i
        if prime_min == 0:
            prime_min = i
if prime_sum != 0:
    print(prime_sum)
    print(prime_min)
else:
    print(-1)