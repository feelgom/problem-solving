# 4 6
# 101111
# 101010
# 101011

from collections import deque
import sys
sys.setrecursionlimit(10**6)

input = sys.stdin.readline

N, M = map(int, input().split())

miro = [ input() for _ in range(N)]
distance = [[0 for _ in range(M)] for _ in range(N)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

x = 0;y=0

q = deque()
def func(miro, a,b):
    if a == N-1 and b == M-1:
        print(distance[N-1][M-1] + 1)
        return
    
    for i in range(4):
        nx = a + dx[i]
        ny = b + dy[i]

        if nx<0 or nx>=N or ny<0 or ny>=M:
            continue
        elif miro[nx][ny] == '1' and distance[nx][ny] == 0:
            q.append([nx,ny])
            distance[nx][ny] = distance[a][b] +1
    
    v = q.popleft()
    x=v[0];y=v[1]
    func(miro,x,y)

func(miro, 0,0)
# print(distance)




