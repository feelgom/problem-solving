lis = [1, 6]
for i in range(2,1000000):
    lis.append(i*6)
    
N = int(input())
ans = 0
sum_ = 0
while N > sum_:
    sum_ += lis[ans]
    ans += 1
    
print(ans)