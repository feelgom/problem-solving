A,B = input().split()
ans = 0

longest = max(len(A), len(B))
A = A.zfill(longest)
B = B.zfill(longest)

add = 0
for i in range(longest):
    S = int(A[-1-i]) + int(B[-1-i]) + add
    add = S//10
    ans += (S%10) * (10**i)

if add > 0:
    ans += add * (10**longest)
print(ans)