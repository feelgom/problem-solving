import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def DFS(x,y):
    farm[x][y] = 0
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]

        if nx<0 or ny<0 or nx>=N or ny>=M:
            return
        elif farm[nx][ny] == 1:
            DFS(nx,ny)

ans = []
T = int(input())
for _ in range(T):
    N,M,K = map(int,input().split())
    farm = [ [0 for _ in range(M)] for _ in range(N)]
    
    for i in range(K):
        x,y = map(int,input().split())
        farm[x][y] = 1

    count = 0
    for i in range(N):
        for j in range(M):
            if farm[i][j] == 1:
                count +=1
                DFS(i,j)

    ans.append(count)

for x in ans:
    print(x)