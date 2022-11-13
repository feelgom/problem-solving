#%%
# 시간초과를 대비하기 위해서는 input() 대신 sys.stdin.readline().strip() 사용하자
import sys
N, M = map(int, input().split())

dogam_dict1 = {}
dogam_dict2 = {}
for i in range(N):
    name = sys.stdin.readline().strip()
    dogam_dict1[name] = i+1
    dogam_dict2[str(i+1)] = name

for _ in range(M):
    q = sys.stdin.readline().strip()
    if ord(q[0]) in range(48,58):
        print(dogam_dict2[q])
        
    else:
        print(dogam_dict1[q])
