#%%
N, M = map(int, input().split())

dogam_dict1 = {}
dogam_dict2 = {}
for i in range(N):
    name = input()
    dogam_dict1[name] = i+1
    dogam_dict2[str(i+1)] = name
    
# dogam = input().split()

#%%
for _ in range(M):
    q = input()
    if ord(q[0]) in range(48,58):
        print(dogam_dict2[q])
        
    else:
        print(dogam_dict1[q])
