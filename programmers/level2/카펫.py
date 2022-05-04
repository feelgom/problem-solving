# https://programmers.co.kr/learn/courses/30/lessons/42842

def solution(brown, yellow):
    answer = []
    # brown = 2*x + 2*y - 4 
    # yellow = (x-2) * (y-2) = xy - 2*(x + y) + 4
    
    x_plus_y = (brown + 4)//2
    x_times_y = brown + yellow
    
    for x in range(3, (x_plus_y)//2 + 1 ):
        if x * (x_plus_y - x) == x_times_y:
            return [x_plus_y-x, x]
   