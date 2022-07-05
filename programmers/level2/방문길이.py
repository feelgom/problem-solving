# https://programmers.co.kr/learn/courses/30/lessons/49994

import numpy as np

def solution(dirs):
    world = np.zeros([11,11,4])
    x, y = 5,5
    move_dict = {"U":[0,1], "D":[0,-1], "R":[1,0], "L":[-1,0]}
    idx_dict = {"U":[0,1], "D":[1,0], "R":[2,3], "L":[3,2]}

    for char in dirs:
        dx, dy = move_dict[char]
        idx1, idx2 = idx_dict[char]
        nx = x+dx
        ny = y+dy
        if nx in range(11) and ny in range(11):
            world[x][y][idx1] = 0.5
            world[nx][ny][idx2] = 0.5
            
            x, y = nx, ny
    
    return int(np.sum(world))