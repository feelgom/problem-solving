# https://programmers.co.kr/learn/courses/30/lessons/12973

def solution(string):
    temp = []
    s = list(string)
    if len(s) <= 1:
        return 0
    a = s.pop()
    lenlen = len(s)
    
    for i in range(2*lenlen):
        if len(s) == 0:
            return 0
        b = s.pop()
        
        if a == b:
            if len(temp) == 0 and len(s) == 0:
                return 1
            elif len(temp) != 0:
                a = temp.pop()
            elif len(s) != 0:
                a = s.pop()
            
        elif a != b:
            if len(s) == 0:
                return 0
            temp.append(a)
            a = b
            
if __name__ == "__main__":
    s = 'baabaa'
    print(solution(s))