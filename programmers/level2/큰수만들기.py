# https://programmers.co.kr/learn/courses/30/lessons/42883
    
def solution(number, k):
    num_list = list(number)
    num_list = [int(elem) for elem in num_list]
    ans_list = []
    while len(num_list) > k and k > 0:
        if 9 in num_list[:k+1]:
            num_max = 9
        else:
            num_max = max(num_list[:k+1])

        ans_list.append(str(num_max))
        idx = num_list.index(num_max)
        num_list = num_list[idx+1:]
        k -= idx
    
    if k == 0:
        for elem in num_list:
            ans_list.append(str(elem))
    
    return "".join(ans_list)


if __name__=="__main__":
    number = "4177252841"
    k = 4
    answer = "775841"
    # print(solution(number,k)==answer, solution(number,k))
    print(solution("98576555",4))