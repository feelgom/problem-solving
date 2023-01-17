num = int(input())

a0 = num // 10
b0 = num % 10

count = 0
a = a0
b = b0
while True:
    count += 1
    temp = a+b
    a = b
    b = temp % 10
    if a == a0 and b == b0:
        break
print(count)
    
    
