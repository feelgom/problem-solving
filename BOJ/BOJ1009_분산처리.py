T = int(input())

dic = {1:1, 2:4, 3:4, 4:2, 5:1, 6:1, 7:4, 8:4, 9:2}
for _ in range(T):
    a,b = map(int, input().split())
    a_one = a%10
    if a_one == 0:
        print(10)
        continue
    else:
        num = dic[a_one]
        b_new = b%num
        if b_new == 0:
            b_new = num
        print((a**b_new)%10)
    
        