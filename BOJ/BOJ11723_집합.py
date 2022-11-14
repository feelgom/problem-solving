#%%
import sys
M = int(input())

sets = [0]*21
for _ in range(M):
    input_list = sys.stdin.readline().strip().split()
    # input_list = input().split()
    action = input_list[0]
    if len(input_list) == 2:
        num = int(input_list[1])
    
    if action == "add":
        sets[num] = 1
    elif action == "remove":
        sets[num] = 0
    elif action == "check":
        print(sets[num])
    elif action == "toggle":
        sets[num] = 1-sets[num]
    elif action == "all":
        sets = [1]*21
    elif action == "empty":
        sets = [0]*21