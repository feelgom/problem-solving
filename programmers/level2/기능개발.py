# https://programmers.co.kr/learn/courses/30/lessons/42586

import numpy as np
def solution(progresses, speeds):
    a = np.array(progresses)
    b = np.array(speeds)
    
    answer = []
    while len(a) > 0:
        count = 0
        a += b 
        while a[0] >= 100:
            a = np.delete(a,0)
            b = np.delete(b,0)
            count += 1

            if len(a) == 0:
                answer.append(count)
                break
            if a[0] < 100:
                answer.append(count)
                break

    return answer

if __name__ == "__main__":
    progresses = [93, 30, 55]
    speeds = [1, 30, 5]
    print(solution(progresses, speeds))
