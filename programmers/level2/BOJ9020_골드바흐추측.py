# 소수 판별 함수
def is_prime_number(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

lis = [0]*500000

for i in range(1,500000):
    if is_prime_number(i):
        lis[i] = 1

T = int(input())
# 골드바흐 파티션 구하기
for _ in range(T):
    n = int(input())
    a = 2
    b = n - 2
    for i in range(2, int(n/2) + 1):
        if lis[i] and lis[n-i]:
            a = i
            b = n - i

    print(a, b)