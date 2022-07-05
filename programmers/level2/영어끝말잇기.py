# https://school.programmers.co.kr/learn/courses/30/lessons/12981

def solution(n, words):
    already = [words[0]]
    for i in range(1,len(words)):
        if already[-1][-1] != words[i][0]:
            break
        if words[i] in already:
            break
        else:
            already.append(words[i])
    else:
        return [0,0]
    
    return[i%n+1, i//n+1]