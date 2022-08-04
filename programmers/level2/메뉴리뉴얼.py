import string
from itertools import combinations

uppers = list(string.ascii_uppercase)

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
        # print(orders)
        char_set = set()
        for order in orders:
            char_set = char_set.union(set(order))
        
        # print(n, char_set)
        combi = list(combinations(char_set, n))
        # print(combi)

        cand = []
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
            # print(com)
            tt = "".join(com)
            if count > max_count:
                cand = [tt]
                max_count = count
            elif count == max_count:
                cand.append(tt)

        print(cand, max_count)
        answer += cand
        
    answer.sort()
    return answer

if __name__=="__main__":
    orders = ["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"]
    course = [2,3,4]
    results = ["AC", "ACDE", "BCFG", "CDE"]

    answer = solution(orders, course)
    print(answer == results, answer)