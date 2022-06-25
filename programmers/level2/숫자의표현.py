# https://programmers.co.kr/learn/courses/30/lessons/12924

def linear_sum(n):
    return n*(n+1)/2

def solution(n):
    answer = 0
    count = 1
    stop = False
    while not stop:
        for i in range(count, n+1):
            if linear_sum(i)-linear_sum(i-count) < n:
                continue            
                
            elif linear_sum(i)-linear_sum(i-count) == n:
                answer += 1
            
            if i == count:
                stop = True
            count += 1
            break
            
    return answer