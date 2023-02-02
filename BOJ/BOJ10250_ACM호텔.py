T = int(input())

for _ in range(T):
    H,W,N = map(int,input().split())
    room = (N-1) // H +1
    floor = (N-1) % H +1
    print(str(floor)+str(room).zfill(2))