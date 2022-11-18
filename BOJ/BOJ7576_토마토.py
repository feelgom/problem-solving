#%%
from collections import deque
M, N = map(int,input().split())

box = []
for _ in range(N):
   box.append(list(map(int,input().split()))) 
#%%
def main():
    queue = deque([])
    zero_count = 0
    for y in range(N):
        for x in range(M):
            if box[y][x] == 1:
                queue.append([y, x])
            if box[y][x] == 0:
                zero_count += 1
                
    if zero_count == 0:
        print(0)
        return 
    
    move = [[1,0],[-1,0],[0,1],[0,-1]]
    while queue:
        y, x = queue.popleft()
        for dx, dy in move:
            nx = x+dx
            ny = y+dy
            if nx<0 or nx>=M or ny<0 or ny>=N:
                continue
            if box[ny][nx] == 0:
                box[ny][nx] = box[y][x] + 1
                queue.append([ny,nx])
            
    max_val = -99
    end=False
    for y in range(N):
        for x in range(M):
            if box[y][x] == 0:
                print(-1)
                return
            else:
                if box[y][x] > max_val:
                    max_val = box[y][x]
                    
    print(max_val-1)
    return

main()