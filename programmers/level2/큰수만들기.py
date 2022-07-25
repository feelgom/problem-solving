# https://programmers.co.kr/learn/courses/30/lessons/42883
# Sol1. 은 짧은 범위 탐색을 통해서 문제를 풀어보려고 시도했으나, 테스트10번 시간초과 문제를 해결하지 못했다.
# Sol2. 는 스택을 이용해서 간단하게 문제를 해결할 수 있었다.

## Sol1.
# def solution(number, k):
#     num_list = list(number)
#     num_list = [int(elem) for elem in num_list]
#     ans_list = []
#     while len(num_list) > k and k > 0:
#         if 9 in num_list[:k+1]:
#             num_max = 9
#         else:
#             num_max = max(num_list[:k+1])

#         ans_list.append(str(num_max))
#         idx = num_list.index(num_max)
#         num_list = num_list[idx+1:]
#         k -= idx
    
#     if k == 0:
#         for elem in num_list:
#             ans_list.append(str(elem))
    
#     return "".join(ans_list)

    
# Sol2.
def solution(number,k):
    stack=[]
    
    for num in number:
        while k > 0 and len(stack)>0 and num > stack[-1]:
            stack.pop()
            k -= 1
        stack.append(num)

    for _ in range(k):
        stack.pop()

    return "".join(stack)

if __name__=="__main__":
    number = "4177252841"
    k = 4
    answer = "775841"
    # print(solution(number,k)==answer, solution(number,k))
    print(solution("98576555",4))