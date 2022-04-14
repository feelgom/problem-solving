# https://programmers.co.kr/learn/courses/30/lessons/42890

import numpy as np
from itertools import combinations

def solution(relation):
    arr = np.array(relation)
    row, col = arr.shape

    key = []
    candidates = []
    a = [i for i in range(col)]
    for i in range(1,col+1):
        c = combinations(a,i)
        candidates.extend(c)

    for cand in candidates:
        select = arr[:,list(cand)]
        select_join = ["".join(elem) for elem in select]
        if len(set(select_join)) == row:
            overlap = False
            for old in key:
                if set(cand).intersection(set(old)) == set(old):
                    overlap =True
                    break
            if not overlap:
                key.append(cand)
    
    return len(key)

relation = [["100","ryan","music","2"],["200","apeach","math","2"],["300","tube","computer","3"],["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","music","2"]]
print(solution(relation))