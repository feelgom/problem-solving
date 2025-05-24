import math
import os
import random
import re
import sys
from collections import deque


def check_valid(a: list[list[str, int]], b: dict[str, int]):
    for c, count in a:
        if b[c] < count:
            return False
    else:
        return True

def steadyGene(gene: str) -> int:
    n = len(gene)
    threshold = [[c, max(gene.count(c) - n//4, 0)] for c in "ATGC" if max(gene.count(c) - n//4, 0) > 0]
    if not threshold:
        return 0
    
    cand = set([c for c, _ in threshold])
    val_dict = {c: 0 for c, _ in threshold}
    min_ans = math.inf
    sub_string_queue = deque()
    for index, letter in enumerate(gene):
        if letter not in cand:
            continue
        
        sub_string_queue.append([index, letter])
        val_dict[letter]+=1
        while check_valid(threshold, val_dict):
            min_ans = min(min_ans, sub_string_queue[-1][0]-sub_string_queue[0][0]+1)
            elem = sub_string_queue.popleft()
            val_dict[elem[1]]-=1

    return min_ans
        
        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    gene = input()

    result = steadyGene(gene)

    fptr.write(str(result) + '\n')

    fptr.close()
