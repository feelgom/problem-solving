# https://programmers.co.kr/learn/courses/30/lessons/42883

def solution(number, k):
    ans_list = []
    num_list = list(number)
    num_list = [int(elem) for elem in num_list]
    
    while 1:
        for i in range(len(num_list)-1):
            if num_list[i] >= num_list[i+1]:
                ans_list.append(num_list[i])
                k-=1
            if k == 0:
                break
        num_list = ans_list
    
    ans_list = [str(elem) for elem in ans_list]
    return "".join(ans_list)

    
# def solution(number, k):
#     num_list = list(number)
#     num_list = [int(elem) for elem in num_list]
#     ans_list = []
#     while len(num_list) > k:
#         if 9 in num_list[:k+1]:
#             num_max = 9
#         else:
#             num_max = max(num_list[:k+1])

#         ans_list.append(str(num_max))
#         idx = num_list.index(num_max)
#         num_list = num_list[idx+1:]
#         k -= idx
    
#     return "".join(ans_list)


if __name__=="__main__":
    number = "4177252841"
    k = 4
    answer = "775841"
    # print(solution(number,k)==answer, solution(number,k))
    print(solution("98576555",4))