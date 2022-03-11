# https://programmers.co.kr/learn/courses/30/lessons/64065

import copy
def solution(s):
    answer = []

    s_splits = s[2:-2].split("},{")
    s_splits.sort(key=len)
    for s_split in s_splits:
        temp = copy.deepcopy(answer)
        numbers = s_split.split(',')
        for number in numbers:
            if int(number) in temp:
                temp.remove(int(number))
            else:
                answer.append(int(number))

    return answer

if __name__ == "__main__":
    s = "{{2},{2,1},{2,1,3},{2,1,3,4}}"
    print(solution(s))