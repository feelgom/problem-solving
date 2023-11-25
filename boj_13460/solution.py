import sys
from collections import deque
from enum import Enum

sys.setrecursionlimit(10**6)
input = sys.stdin.readline

class Dir(Enum):
        UP = 0
        DOWN = 1
        LEFT = 2
        RIGHT = 3
        
move_dict = {
    Dir.UP:  [0, -1],
    Dir.DOWN: [0, 1],
    Dir.LEFT: [-1, 0],
    Dir.RIGHT: [1, 0]
}

class Board:
    def __init__(self, board):
        self.board = board
        self.N=len(board)
        self.M=len(board[0])
        for i in range(N):
            for j in range(M):
                if board[i][j] == 'R':
                    self.R = [j, i]
                elif board[i][j] == 'B':
                    self.B = [j, i]
    
    def move(self, R, B, Dir):
        self.R = R
        self.B = B
        nR = self.moved_pose(self.R, Dir)
        nB = self.moved_pose(self.B, Dir)
        return nR, nB
    
    def moved_pose(self, pos, Dir):
        x,y = pos[:]
        
        blocked = False
        dx, dy = move_dict[Dir]
        while x in range(self.M) and y in range(self.N):
            x, y  = x+dx, y+dy
            if [x, y] == self.R or [x, y] == self.B:
                blocked = True
            
            if self.board[y][x] == '#':
                x, y = x-dx, y-dy
                if blocked:
                    x, y = x-dx, y-dy    
                return [x, y]
            elif self.board[y][x] == 'O':
                return [None, None]

def BFS(count, R, B):
    if count == 10: # 10번 이상 움직이면 실패
        print(-1)
        return True
    
    for dir in Dir:
        nR, nB = board.move(R, B, dir)
        if nB == [None, None]: # 파란 공이 빠져서 실패
            continue
            
        if nR == [None, None]: # 빨간 공이 빠지는 성공 조건
            print(count+1)
            return True
        elif nR != board.R or nB != board.B: # 두 공 중에서 한 공이라도 움직였으면 큐에 추가
            q.append((count+1, nR, nB))

    while q:
        nCount, nR, nB = q.popleft()
        if BFS(nCount, nR, nB):
            return True # 성공조건
        
    else: # 더 이상 갈 곳이 없음
        print(-1)
        return False

if __name__ == "__main__":
    N,M=map(int,input().split())
    board_input = [list(input().rstrip()) for _ in range(N)]
    board = Board(board_input)
    
    q = deque([])
    BFS(0, board.R[:], board.B[:])