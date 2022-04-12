# https://programmers.co.kr/learn/courses/30/lessons/72412
# 전체 케이스에 대해 dictionary를 만들어서 구현했다.
# -> 정확도 테스트는 모두 통과 but 효율성 테스트 시간초과
#   아마 query가 최대 10만개이고, 경우에 따라 최대 for문이 24회까지 돌기 때문인 것 같다.
# -> "-" 이 들어올 것을 고려해서 dic에 "-"를 key로 추가 & dictionary 정의를 for문으로 변경


import numpy as np
import time
def solution(info, queries):
    t1 =time.time()
    dic ={}
    for lang in ["cpp", "java", "python", "-"]:
        dic[lang] = {}
        for pos in ["frontend", "backend", "-"]:
            dic[lang][pos] = {}
            for career in ["junior", "senior", "-"]:
                dic[lang][pos][career] = {}
                for food in ["chicken", "pizza", "-"]:
                    dic[lang][pos][career][food] = []

    t2 = time.time()
    a = t2-t1
    
    for info_i in info:
        tokens = info_i.split(" ")
        for lang in [tokens[0], "-"]:
            for pos in [tokens[1], "-"]:
                for career in [tokens[2], "-"]:
                    for food in [tokens[3], "-"]:
                        dic[lang][pos][career][food].append(int(tokens[4]))
    
    t3 = time.time()
    b = (t3-t2)*50000/6

    # 시간초과 해결을 위한 sorting 작업 추가
    for lang in ["cpp", "java", "python", "-"]:
        for pos in ["frontend", "backend", "-"]:
            for career in ["junior", "senior", "-"]:
                for food in ["chicken", "pizza", "-"]:
                    dic[lang][pos][career][food].sort()

    t4 = time.time()
    c = t4-t3

    ans = []
    for query in queries:
        count = 0
        tokens = query.split(" ")
        language = tokens[0]
        position = tokens[2]
        career = tokens[4]
        food = tokens[6]
        score = int(tokens[7])
        
        cand = dic[language][position][career][food]
        
        # Binary Search
        l = 0
        h = len(cand) - 1
        tmp = -1
        while l <= h:
            m = (l+h)//2

            if cand[m] >= score:
                tmp = m
                h = m - 1
            else:
                l = m + 1
        
        if tmp == -1:
            ans.append(0)
            continue

        count = len(cand) - tmp

        # count = (np.array(dic[language][position][career][food]) >= score).sum() #시간초과 원인
        ans.append(int(count))

    t5 = time.time()
    d = (t5-t4)*100000/6
    print(f"In extreme case, expect {a+b+c} seconds elapsed")
    return ans


if __name__=="__main__":
    info = ["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"]
    query = ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]

    ans =[1,1,1,1,2,4]
    sol = solution(info, query)

    print(ans==sol, sol)