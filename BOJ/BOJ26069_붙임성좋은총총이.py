import sys
input = sys.stdin.readline

N = int(input())
lis = ["ChongChong"]
for _ in range(N):
    A, B = input().strip().split()
    if A in lis or B in lis:
        lis.append(A)
        lis.append(B)
    
print(len(set(lis)))