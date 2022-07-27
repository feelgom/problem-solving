# https://school.programmers.co.kr/learn/courses/30/lessons/68936

import numpy as np

def dnc(arr):
    answer = np.array([0, 0])
    r = arr.shape[0]
    
    if arr.size == 1:
        if sum(arr) == 1:
            return np.array([0, 1])
        else:
            return np.array([1, 0])
        
    if arr.sum() == arr.size:
        return np.array([0, 1])
    elif arr.sum() == 0:
        return np.array([1, 0])
        
    answer += dnc(arr[:r//2,:r//2])
    answer += dnc(arr[:r//2,r//2:])
    answer += dnc(arr[r//2:,:r//2])
    answer += dnc(arr[r//2:,r//2:])
    
    return answer

def solution(arr):
    np_arr = np.array(arr)
    return dnc(np_arr).tolist()

