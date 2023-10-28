def find_index(dp,num):
    start = 0
    end = len(dp)
    while start < end:
        mid = (start+end)//2
        if num <= dp[mid]:
            end = mid
        else:
            start = mid + 1
    return end


N = int(input())
A = list(map(int,input().split()))
dp = [0]

for num in A:
    if num > dp[-1]:
        dp.append(num)
    else:
        idx = find_index(dp,num)
        dp[idx] = num

print(len(dp)-1)