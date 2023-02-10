import math
def is_prime_number(x):
    if x <= 1:
        return False
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False 
    return True

lis = [0]*500000

for i in range(1,500000):
    if is_prime_number(i):
        lis[i] = 1

while 1:
    N = int(input())
    if N == 0:
        break
    print(sum(lis[N+1:2*N+1]))