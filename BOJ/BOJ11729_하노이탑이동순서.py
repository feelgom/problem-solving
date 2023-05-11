def hanoi(start, end, n):
    if n == 1:
        return [[start, end]]
    ans = hanoi(start, (6-start-end), n-1)
    ans += hanoi(start, end, 1)
    ans += hanoi((6-start-end), end, n-1)
    return ans

N = int(input())
ans = hanoi(1,3,N)
print(len(ans))
for elem in ans:
    print(*elem)