# https://programmers.co.kr/learn/courses/30/lessons/12936

facto = [1]
for i in range(1,21):
    facto.append(facto[i-1]*i)

def solution(n, k):
    ans = []
    cand = [i for i in range(1,n+1)]
    
    for j in range(1,n+1):
        index = (k-1) // facto[n-j]
        k = k % facto[n-j]

        ans.append(cand[index])
        cand.remove(cand[index])
    
    return ans