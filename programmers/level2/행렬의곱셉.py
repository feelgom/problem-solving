# https://school.programmers.co.kr/learn/courses/30/lessons/12949

import numpy as np
def solution(arr1, arr2):
    np1 = np.array(arr1)
    np2 = np.array(arr2)
    ans = np1@np2

    return ans.tolist()

