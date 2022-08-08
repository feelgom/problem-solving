# https://school.programmers.co.kr/learn/courses/30/lessons/87946

import itertools

def solution(k, dungeons):
    answer = -1
    
    permute_list = list(itertools.permutations(range(len(dungeons))))
    for permute in permute_list:
        temp = 0
        stamina = k
        for ind in permute:
            if stamina >= dungeons[ind][0]:
                stamina -= dungeons[ind][1]
                temp += 1
                
        if temp > answer:
            answer = temp
        
    return answer