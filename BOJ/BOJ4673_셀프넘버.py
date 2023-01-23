lis = [0] * 20001
for i in range (10001):
    sum = i
    str_i = str(i)
    for num in str_i:
        sum += int(num)
    lis[sum] =1

for i in range(1,10001):
    if lis[i] == 0:
        print(i)
