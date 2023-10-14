N = int(input())
cost = [list(map(int, input().split())) for _ in range(N)]
status = []
for char in input():
    if char == 'Y':
        status.append(True)
    else:
        status.append(False)
P = int(input())

if sum(status) >= P:
    print(0)
elif sum(status) == 0:
    print(-1)

todo = P - sum(status)
ans = 0
for _ in range(todo):
    min_cost = 1000000000
    min_index = -1
    for i, st in enumerate(status):
        if st:
            continue
        for j, cst in enumerate(cost[i]):
            if cst < min_cost and status[j]:
                min_cost = cst
                min_index = i
    status[min_index] = True
    ans += min_cost
    print(min_cost, min_index, status)
    
print(ans)