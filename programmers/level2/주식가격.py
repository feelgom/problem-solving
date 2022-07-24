# https://school.programmers.co.kr/learn/courses/30/lessons/42584

def solution(prices):
    answer = [-999] * len(prices)
    queue = [[0,-1]]
    for ind, price in enumerate(prices):
        if price >= queue[-1][0]:
            queue.append([price, ind])
        else:
            while price < queue[-1][0]:
                _, index = queue.pop()
                answer[index]= ind - index
            queue.append([price,ind])

    for _, index in queue:
        answer[index] = ind- index

    return answer

if __name__=="__main__":
    prices = [1, 2, 3, 2, 3]
    answer = [4, 3, 1, 1, 0]
    print(solution(prices)==answer)