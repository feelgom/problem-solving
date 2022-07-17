# https://school.programmers.co.kr/learn/courses/30/lessons/12952

def promising(i,col):
    if col[i] in col[1:i]:
        return False
    for k in range(1,i):
        if col[i-k] == col[i]-k or col[i-k] == col[i]+k:
            return False
    return True

def n_queen(i, col):
    n = len(col)-1
    if(promising(i,col)):
        if i == n:
            col[0] +=1
            print(col)
        else:
            for j in range(1,n+1):
                col[i+1] = j
                n_queen(i+1,col)

def solution(n):
    col = [0] * (n+1)
    n_queen(0, col)

    return col[0]

if __name__=="__main__":
    n = 4
    answer =2 
    print(solution(n)==answer)