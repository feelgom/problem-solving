# 단지번호붙이기
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N = int(input())
town = [ list(input().rstrip()) for _ in range(N)]


def DFS(x,y):
    global number 
    number +=1
    town[x][y] = str(count+1)
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]  
    for i in range(4):
        nx = x+dx[i];ny=y+dy[i]
        if nx<0 or ny<0 or nx>=N or ny>=N:
            continue
        elif town[nx][ny] == '1':
            DFS(nx,ny)


num = []
count = 0
for i in range(N):
    for j in range(N):
        if town[i][j] == '1':
            count += 1
            number = 0
            DFS(i,j)
            num.append(number)

# print(town)
num.sort()
# print(num)
print(count)
for i in range(count):
    print(num[i])