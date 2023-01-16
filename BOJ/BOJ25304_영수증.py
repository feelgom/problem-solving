total = int(input())
price_sum = 0
N = int(input())
for _ in range(N):
    price, count = map(int, input().split())
    price_sum += price * count
if price_sum == total:
    print("Yes")
else:
    print("No")