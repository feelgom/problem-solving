# https://programmers.co.kr/learn/courses/30/lessons/12939

def solution(s):
    s_list = s.split(' ')
    s_list = [int(elem) for elem in s_list]
    s_list.sort()
    
    return " ".join([str(s_list[0]), str(s_list[-1])])
