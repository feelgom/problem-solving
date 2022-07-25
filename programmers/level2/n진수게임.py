# https://school.programmers.co.kr/learn/courses/30/lessons/17687

import string
N_dic = string.digits + string.ascii_uppercase[:6]

def convert(number, N):
    answer = ""
    q, r = divmod(number,N)
    if q == 0:
        return N_dic[r]
    return convert(q, N) + N_dic[r]


def solution(n,t,m,p):
    index = [p-1+m*i for i in range(t)]
    numbers = ""
    i = 0
    while len(numbers) <= index[-1]:
        numbers += convert(i,n)
        i+=1

    answer = [numbers[ind] for ind in index]
    return "".join(answer)


