# https://programmers.co.kr/learn/courses/30/lessons/42895
#%%
import numpy as np
def solution(N, number):
    dp = [9]*(1000000)
    Q = [N, 11*N, 111*N, 1111*N, 11111*N, 111111*N]
    
    dp[N] = 1
    dp[11*N] = 2
    dp[111*N] = 3
    dp[1111*N] = 4
    dp[11111*N] = 5
    dp[111111*N] = 6
    count = 0
    while len(Q)!=0:
        count += 1
        i = Q.pop(0)
        lst = [i+N, i-N, i//N, i*N]
        for item in lst:
            if item >= 0 and item <= 1000000:
                new = dp[i] + 1
                if new < dp[item]:
                    dp[item] = new
                    Q.append(item)
                    print(count, 'dp[',item,'] = ',new,)
    
    for i in range(100000):
        if 2*i < 100000:
            if dp[2*i] > 2*dp[i]:
                dp[2*i] = 2*dp[i]
        if i*i < 100000:        
            if dp[i*i] > 2*dp[i]:
                dp[i*i] = 2*dp[i]
        if dp[i+1] > dp[i] + 2:
            dp[i+1] = dp[i] + 2

    # print(dp)
    answer = dp[number]
    if answer == 9:
        answer = -1
    return answer


if __name__ == "__main__":
    N = 9
    number = 10101
    print(solution(N, number))