# https://programmers.co.kr/learn/courses/30/lessons/1844
# DFS로 풀 수 있을 것 같다. 
# -> 효율성 테스트 통과 못한다. 미로의 분기가 많아질수록 테스트해야할 경우의 수가 기하급수적으로 많아짐.
# BFS로 시도해보자.

## BFS Solution
def solution(maps):
    queue = [[0,0]]
    dic = [[1,0],[0,1],[-1,0],[0,-1]]
    while len(queue) != 0 and maps[-1][-1] == 1:
        x,y = queue.pop(0)
        count = maps[x][y]
        for dx, dy in dic:
            nx = x+dx
            ny = y+dy
            if nx == 0 and ny == 0:
                continue
            if nx < 0 or ny < 0 or nx >= len(maps) or ny >= len(maps[0]):  
                continue
            if maps[nx][ny] == 1 or maps[nx][ny] > count + 1:
                maps[nx][ny] = count + 1
                if nx == len(maps) and ny == len(maps[0]):
                    break
                queue.append([nx,ny])
    
    answer = maps[-1][-1]
    if answer == 1:
        return -1
    else:
        return  answer


## DFS Solution 

# import sys
# import copy
# sys.setrecursionlimit(10000)

# def solution(maps):
#     x, y = 0,0
#     count = 0
#     answer = DFS(x,y, maps, count)
#     if answer == 9999999999:
#         return -1
#     return answer

# def DFS(x,y, maps,count):
#     maps2 = copy.deepcopy(maps)
#     maps2[x][y] = 2
#     count +=1
#     ans = 9999999999
#     if x == len(maps)-1 and y == len(maps[0]) - 1:
#         return count
#     dic = [[1,0],[0,1],[-1,0],[0,-1]]
#     for dx, dy in dic:
#         nx = x + dx
#         ny = y + dy
#         if nx < 0 or ny < 0 or nx >= len(maps) or ny >= len(maps[0]):  
#             continue
#         if maps[nx][ny] == 1:
#             temp = DFS(nx,ny, maps2, count)
#             ans = min(ans,temp)
        
#     return ans
    

if __name__=="__main__":
    maps = [[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]
    # maps = [[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,0],[0,0,0,0,1]]
    print(solution(maps))