# https://programmers.co.kr/learn/courses/30/lessons/62048

from math import gcd

def solution(w,h):
    answer = 1
    
    total = w*h
    minus = w+h
    plus = gcd(w,h)
    
    answer = total - minus + plus
    return answer

if __name__ == "__main__":
    w = 8
    h = 12
    print(solution(w,h))
