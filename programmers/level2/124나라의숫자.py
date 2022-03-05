# https://programmers.co.kr/learn/courses/30/lessons/12899

def solution(n):
    
    reverseList = []
    saveDict = {1:'1', 2:'2', 0:'4'}
    
    while n > 0:
        reverseList.append( saveDict[n%3] )
        n = (n-1)//3
        
    answer = ("".join(reverseList))[::-1]
    return answer