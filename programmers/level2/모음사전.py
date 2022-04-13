# https://programmers.co.kr/learn/courses/30/lessons/84512?language=python3

def solution(word):
    answer = 0
    word_list = ["-"]*5
    for i in range(len(word)):
        word_list[i] = word[i]
    
    dic = {"A":0, "E":1, "I":2, "O":3, "U":4}
    weight = [781,156,31,6,1]
    
    for i in range(5):
        if word_list[i] == "-":
            return answer
        else:
            answer += dic[word_list[i]] * weight[i] + 1
        
    return answer
        
if __name__=="__main__":
    words = ["AAAAE","AAAE","I","EIO"]
    results = [6, 10, 1563, 1189]

    ans = [solution(word) for word in words]
    print(ans == results, ans)


#     A----       1번째 A E I O U 781씩 차이
#     AA---       2번째 - A E I O U 처음 1 156씩 차이
#     AAA--       3번째 - A E I O U 처음 1 31씩 차이
#     AAAA-       4번째 - A E I O U 처음 1 6씩 차이
#     AAAAA       5번째 - A E I O U 1씩 차이
#     AAAAE
#     AAAAI
#     AAAAO
#     AAAAU
#     AAAE-
    