A = int(input())
B = int(input())
C = int(input())
N = A * B * C
lis = [0]*10

for char in str(N):
    lis[int(char)] += 1

for elem in lis:
    print(elem)