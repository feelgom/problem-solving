num, base = map(int,input().split())

lis = []
while num > 0:
    lis.append(num % base)
    num //= base

ans = ""
for elem in lis[::-1]:
    if elem >= 10:
        ans+= chr(elem + 55)
    else:
        ans+= str(elem)

print(ans)