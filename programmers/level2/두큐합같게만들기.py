# https://school.programmers.co.kr/learn/courses/30/lessons/118667

from collections import deque

def solution(queue1, queue2):
    count_max = len(queue1) + len(queue2)
    total = sum(queue1) + sum(queue2)
    queue1 = deque(queue1)
    queue2 = deque(queue2)
    
    if total % 2 != 0:
        return -1
    
    target = total/2
    count = 0
    sum1 = sum(queue1)
    sum2 = sum(queue2)
    while sum1 != target and count < count_max+4:
        if sum1 > target:
            temp = queue1.popleft()
            queue2.append(temp)
            sum1 -= temp
            sum2 += temp
        else:
            temp = queue2.popleft()
            queue1.append(temp)
            sum2 -= temp
            sum1 += temp
            
        count +=1
        
    if count >= count_max+4:
        return -1
    return count

if __name__ == "__main__":
    queue1 = [1, 2, 1, 2]
    queue2 = [1, 10, 1, 2]
    result = 7
    print(solution(queue1, queue2)==result)
