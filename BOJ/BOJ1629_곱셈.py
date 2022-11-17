#%%
A,B,C = map(int, input().split())

t = A%C

lis = [0]*31
lis[0] = t
for i in range(1,31):
    t = t ** 2
    t = t % C
    lis[i] = t
    
binary = []
while B > 0:
    binary.append(B%2)
    B = B//2

ans = 1
for i in range(len(binary)):
    if binary[i] == 1:
        ans *= lis[i]

print(ans%C)
