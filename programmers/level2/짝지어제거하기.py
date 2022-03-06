# https://programmers.co.kr/learn/courses/30/lessons/12973

def solution(s):    
    i=0
    while i < len(s)-1:
        if s[i] == s[i+1]:
            s = s[:i] + s[i+2:]
            deleted = 1
            i -= 1
            if i<0:
                i = 0
            continue
        i+= 1
    
    if len(s) == 0 :
        return 1
    else:
        return 0 
    

if __name__ == "__main__":
    s = 'baabaa'
    print(solution(s))