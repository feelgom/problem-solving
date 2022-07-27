# https://school.programmers.co.kr/learn/courses/30/lessons/87389

def solution(n):
    n -= 1
    for i in range(2,n+1):
        if n%i == 0:
            return i

