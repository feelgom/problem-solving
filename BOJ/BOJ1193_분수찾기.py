N = int(input())

i=1
while N > i*(i+1)/2:
    i+=1

a = int(N-(i-1)*i/2)
b = int(i-a+1)
if i%2 ==0:
    print(f'{a}/{b}')
else:
    print(f'{b}/{a}')
