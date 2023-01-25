lis = list(input())
ans = [-1]*26
for i in range(26):
    if chr(i+97) in lis:
        ans[i] = lis.index(chr(i+97))
        
print(*ans)