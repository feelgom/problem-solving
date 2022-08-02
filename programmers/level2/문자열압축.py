# https://school.programmers.co.kr/learn/courses/30/lessons/60057

def solution(s):
    if len(s) == 1:
        return 1
    cands = []
    for l in range(1,len(s)//2+1):
        print('l=',l)
        i=0
        local_answer = 0
        while i+l<=len(s):
            count = 1
            key = s[i:i+l]
            j= i+l
            if j+l > len(s):
                local_answer += len(key)
                print(local_answer, str(count)+key)
                i = i+l
                break
            
            while j+l<=len(s):
                print("l=",l," i=",i," j=",j)
                print(s[j:j+l], key)
                if s[j:j+l] == key:
                    count +=1
                    j = j+l
                else:
                    break
            if count >1:
                local_answer += len(key) + len(str(count))
            else:
                local_answer += len(key)
            print(local_answer, str(count)+key)
            i = j

        #while end
        local_answer += len(s)-i
        print("final local answer", local_answer)
        cands.append(local_answer)
    print("cands=", cands)

    return min(cands)

if __name__=="__main__":
    s = ["aaaaaaaaaaaabcd","aabbaccc","ababcdcdababcdcd","abcabcdede","abcabcabcabcdededededede","xababcdcdababcdcd"]
    results = [6,7,9,8,14,17]

    ans = [solution(word) for word in s]
    print(ans == results, ans)