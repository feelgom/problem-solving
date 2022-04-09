# https://programmers.co.kr/learn/courses/30/lessons/12985

import math
def solution(n,a,b):
    while 1:
        if (a-1)//n == (b-1)//n:
            answer = int(math.log2(n))
            n /= 2    
        else:
            break

    return answer

if __name__=="__main__":
    n ,a, b = 8, 4, 7;
    print(solution(n,a,b))