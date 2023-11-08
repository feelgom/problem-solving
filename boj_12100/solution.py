from enum import Enum
import copy
    
class Dir(Enum):
    UP = 0
    DOWN = 1
    LEFT = 2
    RIGHT = 3

def move(board, dir):
    if dir == Dir.UP:
        for i in range(N):
            q = []
            for j in range(N):
                if board[j][i] == 0:
                    continue
                if len(q) == 0 or q[-1] != board[j][i]:
                    q.append(board[j][i])
                elif q[-1] == board[j][i]:
                    q.pop()
                    q.append(board[j][i]*2+1)

            for j in range(N):
                if j < len(q):
                    if q[j] % 2 == 0:
                        board[j][i] = q[j]
                    else:
                        board[j][i] = q[j]-1
                else:
                    board[j][i] = 0
        
    elif dir == Dir.DOWN:
        for i in range(N):
            q = []
            for j in range(N-1, -1, -1):
                if board[j][i] == 0:
                    continue
                if len(q) == 0 or q[-1] != board[j][i]:
                    q.append(board[j][i])
                elif q[-1] == board[j][i]:
                    q.pop()
                    q.append(board[j][i]*2+1)

            for j in range(N):
                if j < len(q):
                    if q[j] % 2 == 0:
                        board[N-1-j][i] = q[j]
                    else:
                        board[N-1-j][i] = q[j]-1
                else:
                    board[N-1-j][i] = 0
        
    elif dir == Dir.LEFT:
        for j in range(N):
            q = []
            for i in range(N):
                if board[j][i] == 0:
                    continue
                if len(q) == 0 or q[-1] != board[j][i]:
                    q.append(board[j][i])
                elif q[-1] == board[j][i]:
                    q.pop()
                    q.append(board[j][i]*2+1)

            for i in range(N):
                if i < len(q):
                    if q[i] % 2 == 0:
                        board[j][i] = q[i]
                    else:
                        board[j][i] = q[i]-1
                else:
                    board[j][i] = 0
        
    elif dir == Dir.RIGHT:
        for j in range(N):
            q = []
            for i in range(N-1, -1, -1):
                if board[j][i] == 0:
                    continue
                if len(q) == 0 or q[-1] != board[j][i]:
                    q.append(board[j][i])
                elif q[-1] == board[j][i]:
                    q.pop()
                    q.append(board[j][i]*2+1)

            for i in range(N):
                if i < len(q):
                    if q[i] % 2 == 0:
                        board[j][N-1-i] = q[i]
                    else:
                        board[j][N-1-i] = q[i]-1
                else:
                    board[j][N-1-i] = 0
    else:
        print(1)

def action(board, depth):
    ans = max(map(max, board))
    if depth == 5:
        return ans
    
    for dir in Dir:
        moved_board = copy.deepcopy(board)
        move(moved_board, dir)
        if board != moved_board:
            temp = action(moved_board, depth+1)
            ans = max(ans, temp)
    
    return ans
        

N = int(input())
board = []
for _ in range(N):
    board.append(list(map(int, input().split())))

ans = action(board, 0)
print(ans)