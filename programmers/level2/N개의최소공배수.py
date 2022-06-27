# https://programmers.co.kr/learn/courses/30/lessons/12953

def gcd(a,b):
    i = min(a,b)
    while i != 0:
        if a%i == 0 and b%i ==0:
            return i
        else:
            i -= 1

def lcm(a,b):
    return a*b/gcd(a,b)
    

def solution(arr):
    ans = arr[0]
    for i in range(1,len(arr)):
        ans = lcm(ans,arr[i])
    
    return ans
