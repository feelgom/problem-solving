a = list(map(int,input().split()))
sum = 0
for num in a:
    sum+= num**2
print(sum%10)