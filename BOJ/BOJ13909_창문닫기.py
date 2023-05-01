N = int(input())
ans = 0
i = 0
while True:
    i += 1
    if i**2 > N:
        break
    else:
        ans +=1
        
print(ans) 