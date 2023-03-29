fibo = [0,1]

N = int(input())

for _ in range(N):
    fibo.append(fibo[-1] + fibo[-2])

print(fibo[N], N-2)