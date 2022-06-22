# https://programmers.co.kr/learn/courses/30/lessons/12900

sol = [0]*60001
sol[1] = 1
sol[2] = 2
for i in range(3,60001):
    sol[i] = sol[i-1] + sol[i-2]

def solution(n):
    return sol[n] % 1000000007

if __name__=="__main__":
    n = 4
    answer = 5
    print(solution(n) == answer, solution(n))