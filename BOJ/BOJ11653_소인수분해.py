import math
def has_divisor(x):
    if x <= 1:
        return -1
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return i
    return 0

N = int(input())
while N != 1:
    div = has_divisor(N)
    if div == 0:
        print(N)
        break
    else:
        print(div)
        N //= div
    