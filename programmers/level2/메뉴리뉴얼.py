# https://school.programmers.co.kr/learn/courses/30/lessons/72411

from itertools import combinations

def solution(orders, course):
    length = [len(order) for order in orders]
    length.sort()
    if length[-1] == length[-2]:
        max_length = length[-1]
    else:
        max_length = length[-2]

    answer = []
    for n in course:
        if n > max_length:
            break
        orders = [order for order in orders if len(order)>=n]
        
        combi = set()
        for order in orders:
            combi = combi | set(combinations(order, n))

        cand = set()
        max_count = 2
        for com in combi:
            count = 0
            for order in orders:
                for i in range(n):
                    if com[i] not in order:
                        break
                else:
                    count+=1
            com = list(com)
            com.sort()
            tt = "".join(com)
            if count > max_count:
                cand = set([tt])
                max_count = count
            elif count == max_count:
                cand = cand | set([tt])

        answer += list(cand)
        
    answer.sort()
    return answer

if __name__=="__main__":
    orders = ["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"]
    course = [2,3,4]
    results = ["AC", "ACDE", "BCFG", "CDE"]

    answer = solution(orders, course)
    print(answer == results, answer)