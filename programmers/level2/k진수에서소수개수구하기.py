# https://school.programmers.co.kr/learn/courses/30/lessons/92335

import string
import math

N_dic = string.digits + string.ascii_uppercase[:6]
def convert(number, N):
    answer = ""
    q, r = divmod(number,N)
    if q == 0:
        return N_dic[r]
    return convert(q, N) + N_dic[r]

def is_prime_number(x):
    if x <= 1:
        return False
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False 
    return True

def solution(n, k):
    num = convert(n, k)
    num_split = num.split('0')
    cands = [int(elem) for elem in num_split if len(elem)>0]
    
    answer = 0
    for cand in cands:
        if is_prime_number(cand):
            answer+=1

    return answer