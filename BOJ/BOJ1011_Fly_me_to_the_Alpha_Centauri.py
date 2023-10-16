def min_move(distance):
    move = 0
    count = 1
    count_up = True
    while distance > 0:
        distance -= count
        move += 1
        count_up = not count_up
        if count_up:
            count += 1
    
    return move
        
N=int(input())
for _ in range(N):
    start,end = map(int,input().split())
    
    ans = min_move(end-start)
    print(ans)
