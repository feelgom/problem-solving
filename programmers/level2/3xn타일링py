# https://programmers.co.kr/learn/courses/30/lessons/12902

sol = [0]*5001
sol[2] = 3
sol[4] = 11
for i in range(6,5001):
    if i%2 == 0:
        sol[i] = sol[i-2]*4 - sol[i-4]


def solution(n):
    return sol[n] % 1000000007

if __name__=="__main__":
    n = 4
    answer = 11
    print(solution(n) == answer, solution(n))