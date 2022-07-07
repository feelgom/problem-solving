# https://school.programmers.co.kr/learn/courses/30/lessons/12951

def solution(s):
    s_list = list(s)
    answer_list = []
    prev = " "
    for char in s_list:
        if prev == " " and ord(char) >= 97 and ord(char) <= 122:
            new = chr(ord(char)-32)
            answer_list.append(new)
        elif prev != " " and ord(char) >= 65 and ord(char) <= 90:
            new = chr(ord(char)+32)
            answer_list.append(new)
        else:
            answer_list.append(char)
        prev = char
        
    return "".join(answer_list)