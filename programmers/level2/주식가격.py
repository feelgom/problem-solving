# https://school.programmers.co.kr/learn/courses/30/lessons/42584

def solution(prices):
    answer = []
    queue = [[0,-1]]
    for ind, p in enumerate(prices):
        if p >= queue[-1][0]:
            queue.append([p, ind])
        else:
            while p < queue[-1][0]:
                answer.append(p)

    return answer