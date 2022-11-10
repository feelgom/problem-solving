#%%

R, C = map(int,input().split())

world = []
visit = []
for _ in range(R):
    world.append(input())
    
visit.append(world[0][0])