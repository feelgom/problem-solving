
# https://programmers.co.kr/learn/courses/30/lessons/12909

def solution(s):
    count = 0
    for elem in s:
        if elem == "(":
            count += 1
        elif elem == ")":
            count -= 1
        
        if count < 0:
            return False

    return count == 0

