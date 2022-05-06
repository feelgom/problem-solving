# https://programmers.co.kr/learn/courses/30/lessons/12905
# sol1. 정확성 테스트는 통과하지만 효율성 테스트에서 시간초과
# -> np.sum안에서 반복문이 돌기 때문에 시간초과가 발생하는 것 같다.
# sol2. 반복을 최소화하기 위해서 DP 이용한 풀이
# -> 맨 오른쪽 아래 꼭짓점의 좌표가 (x,y)인 정사각형의 최대 크기는 
# (x-1,y-1), (x-1,y), (x,y-1) 이 세 점에서의 최대 크기에 의해 결정된다.

## sol 1
# import numpy as np
# def solution(board):
#     board = np.array(board)
#     length = min(board.shape)
    
#     board_sum = board.sum()
    
#     while length >= 1:
#         if length**2 > board_sum:
#             length -= 1
#             continue
            
#         for y in range(board.shape[0]-length+1):
#             for x in range(board.shape[1]-length+1):
#                 if board[y:y+length,x:x+length].sum() == length**2:
#                     return length **2
                
#         length -= 1
        
#     return 0


# sol 2
def solution(board):
    answer = max(board[0])
    for y in range(1,len(board)):
        for x in range(1,len(board[0])):
            if board[y][x] == 1:
                board[y][x] = min(board[y-1][x-1], board[y-1][x], board[y][x-1])+1
        answer = max(answer, max(board[y]))

    return answer**2