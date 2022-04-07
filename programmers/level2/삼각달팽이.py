# https://programmers.co.kr/learn/courses/30/lessons/68645

import numpy as np
def solution(n):
    move_dict = {
        0: [0, 1],
        1: [1 ,0],
        2: [-1,-1]
    }
    
    arr = np.zeros([n,n])
    x, y = 0, -1
    count = 1
    
    for k in range(n):
        length = n - k
        dx, dy = move_dict[k%3]
        for i in range(length):
            x += dx
            y += dy
            arr[y][x] = count
            count += 1
            
    temp = []
    for i in range(n):
        temp += arr[i].tolist()
    answer = [ int(s) for s in temp if s >0]
    
    return answer

if __name__=="__main__":
    n = 6
    print(solution(n))