n,k = map(int,input().split())
arr = list(map(int,input().split()))
ans = 0
for i in range(n):
    if arr[i] >= arr[k-1] and arr[i] > 0:
        ans += 1
print(ans)