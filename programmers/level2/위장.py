# https://programmers.co.kr/learn/courses/30/lessons/42578

def solution(clothes):
    answer = 1
    dic = {}
    for cloth in clothes:
        if cloth[1] not in dic:
            dic[cloth[1]] = []
        dic[cloth[1]].append(cloth[0])

    for elem in dic.values():
        answer *= len(elem)+1

    return answer-1

if __name__=="__main__":
    clothes = [["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]]
    print(solution(clothes))