import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)

def is_palindrome(s):
    return s == s[::-1]

N=int(input())
nums = list(map(int,input().split()))

arr = [[-1]*N for _ in range(N)]
def is_palindrome(i,j):
    if i==j:
        return 1
    elif j == i+1:
        if nums[i] == nums[j]:
            return 1
        else:
            return 0
    else:
        if arr[i][j] != -1:
            return arr[i][j]
        if nums[i] != nums[j]:
            arr[i][j] = 0
        else:
            arr[i][j] = is_palindrome(i+1,j-1)
        return arr[i][j]
            

M = int(input())
for _ in range(M):
    a,b = map(int,input().split())
    print(is_palindrome(a-1,b-1))