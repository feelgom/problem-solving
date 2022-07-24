# https://programmers.co.kr/learn/courses/30/lessons/12946
# 함수의 재귀 호출과정이 궁금하다면 hanoi_with_logs 함수 참고

def solution(n):
    # hanoi_with_logs(1,3,n)
    return hanoi(1,3,n)

def hanoi(start, end, n):
    if n == 1:
        return [[start, end]]
    ans = hanoi(start, (6-start-end), n-1)
    ans += hanoi(start, end, 1)
    ans += hanoi((6-start-end), end, n-1)
    return ans

def hanoi_with_logs(start, end, n, space=""):
    space += " "
    print(space,"input hanoi", start, end, n)
    if n == 1:
        print(space,"move", start, end)
        print(space,"output hanoi", start, end, n)
        return [[start, end]]
    ans = []
    
    lists = [1,2,3]
    lists.remove(start)
    lists.remove(end)
    ans += hanoi_with_logs(start, lists[0], n-1, space)

    ans += [[start,end]]
    print(space,"move", start, end)

    ans += hanoi_with_logs(lists[0], end, n-1, space)
    
    print(space,"output hanoi", start, end, n) 
    return ans