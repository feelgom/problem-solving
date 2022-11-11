#%%
# R, C = map(int,input().split())

world = []
visit = []
# for _ in range(R):
#     world.append(input())
    
# score = [[0]*C]*R
world =[
'HFDFFB',
'AJHGDH',
'DGAGEH']

y, x= 0, 0
move = [[1,0], [-1,0], [0,1], [0,-1]]    

def DFS(x, y, visit):
    visit.append(world[y][x])
    max_score = len(visit)
    for dx,dy in move:
        nx = x+dx
        ny = y+dy
        if nx >=0 and nx < C and ny >= 0 and ny < R and world[ny][nx] not in visit:
            score_ = DFS(nx, ny, visit)
            print(score_, max_score)
            if score_ > max_score:
                max_score = score_
            
    return max_score    



