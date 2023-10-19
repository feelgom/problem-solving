from math import inf

N, M = map(int, input().split())
nums = list(map(int, input().split()))

start = 0
end = 0
ans = inf

sum_nums = 0
while 1:
    if sum_nums >= M:
        start += 1
        sum_nums -= nums[start - 1]
    else:
        if end == N:
            break
        end += 1
        sum_nums += nums[end - 1]

    if sum_nums >= M:
        if ans > end - start:
            ans = end - start


if ans == inf:
    print(0)
else:
    print(ans)
