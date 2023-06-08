import sys
input = sys.stdin.readline

while True:
    a = input()
    if not a:
        break
    N, S = map(int,a.split())
    print(S//(N+1))