# https://programmers.co.kr/learn/courses/30/lessons/17684

def solution(msg):
    answer = []
    dic = {}
    for i in range(1,27):
        dic[chr(i+64)] = i
    
    index = 27
    
    i = 0
    j = 1
    while i < len(msg):
        while msg[i:j] in dic and j <= len(msg):
            j +=1

        j -= 1
        answer.append(dic[msg[i:j]])

        dic[msg[i:j+1]] = index
        index +=1
        i = j
        j+=1
        
    return answer

if __name__=="__main__":
    msg = ["KAKAO", "TOBEORNOTTOBEORTOBEORNOT", "ABABABABABABABAB"]
    answer = [[11, 1, 27, 15], [20, 15, 2, 5, 15, 18, 14, 15, 20, 27, 29, 31, 36, 30, 32, 34], [1, 2, 27, 29, 28, 31, 30]]
    for i in range(len(msg)):
        print(solution(msg[i]) == answer[i],  solution(msg[i]))