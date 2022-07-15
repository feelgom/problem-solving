# https://school.programmers.co.kr/learn/courses/30/lessons/87390

def solution(n, left, right):
    world = []
    q_left, r_left = divmod(left,n)
    q_right, r_right = divmod(right,n)
    range_list = list(range(q_left+1, n+1))
    for i in range(q_left, q_right+1):
        world += [i+1]*i 
        world += range_list
        range_list.pop(0)

    return world[r_left:n*(q_right-q_left)+r_right+1]