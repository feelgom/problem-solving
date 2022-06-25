# https://programmers.co.kr/learn/courses/30/lessons/12911

def solution(n):
    n_bin = "0"+bin(n)[2:]
    n_list = list(n_bin)
    for i in range(1, len(n_list)):
        if n_list[-i] == "1" and n_list[-i-1] == "0":
            n_list[-i] = "0"
            n_list[-i-1] = "1"
            break
            
    if i != 1:
        front = n_list[:-i+1]
        back = n_list[-i+1:]
    else:
        front = n_list
        back = []
    back.sort()
    ans_list = front+back
    ans = "0b"+"".join(ans_list)
    return int(ans,2)
