# https://programmers.co.kr/learn/courses/30/lessons/17676

import numpy as np
def solution(lines):

    starts = []
    ends = []
    answers = []
    for line in lines:
        _, time, length = line.split(" ")
        hour, minute, second = time.split(':')
        end = int(hour) * 3600 + int(minute) * 60 + float(second)
        start = end - float(length[:-1]) + 0.001
        
        ends.append(end)
        starts.append(start)

    starts = np.array(starts)
    ends = np.array(ends)

    for i in range(len(ends)):
        start_time = ends[i]
        end_time = start_time + 0.999

        answers.append(sum((starts[i:] - end_time) < 0.001))

    return int(max(answers))




if __name__ == "__main__":
    lines = [
        "2016-09-15 20:59:57.421 0.351s",
        "2016-09-15 20:59:58.233 1.181s",
        "2016-09-15 20:59:58.299 0.8s",
        "2016-09-15 20:59:58.688 1.041s",
        "2016-09-15 20:59:59.591 1.412s",
        "2016-09-15 21:00:00.464 1.466s",
        "2016-09-15 21:00:00.741 1.581s",
        "2016-09-15 21:00:00.748 2.31s",
        "2016-09-15 21:00:00.966 0.381s",
        "2016-09-15 21:00:02.066 2.62s"
    ]
    # lines = [
    #     "2016-09-15 01:00:04.002 2.0s",
    #     "2016-09-15 01:00:07.000 2s"
    #     ]
    print(solution(lines))
