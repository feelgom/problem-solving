# https://programmers.co.kr/learn/courses/30/lessons/12978
# DFS 접근 -> 53점
# BFS 접근 -> 100점

import numpy as np

def solution(N, road, K):
    answer = 0
    dist = [500000]*(N+1)
    dist[1] = 0
    mat = np.ones([N+1,N+1])*500000
    for a,b,length in road:
        mat[a][b] = min(mat[a][b],length)
        mat[b][a] = min(mat[a][b],length)

    
    answers = [1]
    while True:
        new_answers = []
        for i in answers:
            cands = (np.where(mat[i] <= K-dist[i])[0]).tolist()
            for cand in cands:
                dist[cand] = min(dist[cand], dist[i]+mat[i][cand])
            new_answers += cands

        prev_length = len(answers)
        answers += new_answers
        answers = list(set(answers))
        if len(answers) == prev_length:
            return len(answers)

## DFS Approach
# def solution(N, road, K):
#     answer = 0
#     mat = np.ones([N+1,N+1])*10001
#     for a,b,length in road:
#         mat[a][b] = min(mat[a][b],length)
#         mat[b][a] = min(mat[a][b],length)
        
#     cands, _ = func(1,K,mat)

#     return len(set(cands))+1

# def func(i, th, mat):
#     cands = (np.where(mat[i] <= th)[0]).tolist()
#     new_cands = []
#     for cand in cands:
#         mat[cand][i] = 10001
#         ret_cands, mat = func(cand, th-mat[i][cand], mat)
#         new_cands += ret_cands
    
#     cands += new_cands
#     return cands, mat


if __name__=="__main__":
    # N = 5 
    # road = [[1,2,1],[2,3,3],[5,2,2],[1,4,2],[5,3,1],[5,4,2]]
    # K = 3

    N = 6
    road = [[1,2,1],[1,3,2],[2,3,2],[3,4,3],[3,5,2],[3,5,3],[5,6,1]]
    K = 4

    result = 4
    print(solution(N,road,K) == result, solution(N,road,K))