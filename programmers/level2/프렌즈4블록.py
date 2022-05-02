# https://programmers.co.kr/learn/courses/30/lessons/17679

import numpy as np
def solution(m, n, board):
    board = np.array([list(row) for row in board])
    answer = 0
    
    while True:
        anchors = []
        for i in range(m-1):
            for j in range(n-1):
                if board[i][j] != "X" \
                and board[i][j] == board[i][j+1] \
                and board[i][j] == board[i+1][j] \
                and board[i][j] == board[i+1][j+1]:
                    anchors.append([i,j])
        if len(anchors) == 0:
            return answer
        
        for i, j in anchors:
            if board[i][j] != "X":
                board[i][j] = "X"
                answer +=1
            if board[i][j+1] != "X":
                board[i][j+1] = "X"
                answer +=1
            if board[i+1][j] != "X":
                board[i+1][j] = "X"
                answer +=1
            if board[i+1][j+1] != "X":        
                board[i+1][j+1] = "X"    
                answer +=1

        for j in range(n):
            for i in range(m-1):
                if board[m-i-1][n-j-1] == "X":
                    start = m-i-1
                    bias = 1
                    for k in range(start):
                        while start-k-bias >= 0 and board[start-k-bias][n-j-1] == "X":
                            bias += 1
                        board[start-k][n-j-1] = board[start-k-bias][n-j-1]
                    
                    for k in range(bias):
                        board[k][n-j-1] = "X"
                

if __name__ == "__main__":
    m = 4
    n = 5
    board = ["CCBDE", "AAADE", "AAABF", "CCBBF"]
    answer = 14
    print(solution(m,n,board) == answer, solution(m,n,board))

    m = 6
    n = 6 
    board = ["TTTANT", "RRFACC", "RRRFCC", "TRRRAA", "TTMMMF", "TMMTTJ"]
    answer = 15

    print(solution(m,n,board) == answer, solution(m,n,board))