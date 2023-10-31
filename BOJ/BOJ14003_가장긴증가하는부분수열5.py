from math import inf

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

def find_LCS():
    LCS = []
    lcs_idx = len(arr)-1
    for i in range(len(A)-1, -1, -1):
        if indices[i] == lcs_idx:
            LCS.append(A[i])
            lcs_idx -= 1
            
    return LCS[::-1]

N = int(input())
A = list(map(int,input().split()))
arr = [-inf]
indices = []

for num in A:
    if num > arr[-1]:
        arr.append(num)
        indices.append(len(arr)-1)
    else:
        idx = find_index(arr,num)
        arr[idx] = num
        indices.append(idx)

print(len(arr)-1)
print(*find_LCS())