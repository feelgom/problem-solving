# https://school.programmers.co.kr/learn/courses/30/lessons/12913

def solution(land):
    answer = [0,0,0,0]
    
    for chunk in land:
        max_val, second_max = sorted(answer, reverse=True)[0:2]
        max_ind = answer.index(max_val)
        
        for i in range(4):
            if i != max_ind:
                answer[i] = chunk[i]+max_val
            else:
                answer[i] = chunk[i]+second_max

    return max(answer)