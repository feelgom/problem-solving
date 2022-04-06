# https://programmers.co.kr/learn/courses/30/lessons/42747

def solution(citations):
    citations.sort(reverse=True)

    answer = 0
    for i in range(len(citations)):
        if citations[i] <= i +1:
            answer = max(answer, citations[i])
        else:
            answer = max(answer, i+1)
    return answer

if __name__=="__main__":
    citations = [3,0,6,1,5]
    print(solution(citations))