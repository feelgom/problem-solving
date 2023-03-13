import sys
input = sys.stdin.readline

N,M= map(int, input().split())

board=[]
for _ in range(N):
    board.append(input())

ans = 999999999
for i in range(N-8+1):
    for j in range(M-8+1):
        colors = ["W", "B"]
        for color in colors:
            count = 0
            for y in range(i,i+8):
                for x in range(j,j+8):
                    if (board[y][x] == color) != ((x+y) % 2 == 0):
                        count+=1
            if count < ans:
                ans = count
                
print(ans)