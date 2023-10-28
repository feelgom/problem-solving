import math
import sys
input = sys.stdin.readline

N=int(input())
nums = list(map(int,input().split()))

start = 0
end=N-1
ans_sum = math.inf
ans = []

while start < end:
    tmp = nums[start] + nums[end]
    if abs(tmp) < ans_sum:
        ans_sum = abs(tmp)
        ans = [nums[start],nums[end]]
    if tmp == 0:
        break
    elif tmp < 0:
        start += 1
    else:
        end -= 1
        
print(*ans)