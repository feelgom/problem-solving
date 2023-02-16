import sys
input = sys.stdin.readline

N = int(input())
maxs = [0,0,0]
mins = [0,0,0]
for i in range(N):
    nums = list(map(int,input().split()))
    if i == 0:
        maxs = nums
        mins = nums
    else:
        new_maxs = [0,0,0]
        new_mins = [0,0,0]
        new_maxs[0] = nums[0] + max(maxs[0:2])
        new_maxs[1] = nums[1] + max(maxs)
        new_maxs[2] = nums[2] + max(maxs[1:3])
        new_mins[0] = nums[0] + min(mins[0:2])
        new_mins[1] = nums[1] + min(mins)
        new_mins[2] = nums[2] + min(mins[1:3])
        maxs = new_maxs
        mins = new_mins
        
print(max(maxs), min(mins))