N = int(input())
budgets = list(map(int,input().split()))
budgets.sort()
total = int(input())

for i in range(N):
    if total <= budgets[i]*(N-i):
        print(total//(N-i))
        break
    total -= budgets[i]
else:
    print(budgets[-1])