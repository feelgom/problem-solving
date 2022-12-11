import sys
input = sys.stdin.readline

N = int(input())
lis = [0]*10001
for _ in range(N):
    lis[int(input())] += 1
    
for i in range(1,10001):
    for _ in range(lis[i]):
        print(i)