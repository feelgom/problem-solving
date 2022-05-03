# https://programmers.co.kr/learn/courses/30/lessons/42885

## sol1. 한 배에 탈 수 있는 인원의 제한이 없다고 가정하고 풀이
# def solution(people, limit):
#     people.sort(reverse=True)
#     answer = 0

#     queue = []
#     for person in people:
#         for elem in queue:
#             if elem >= person:
#                 queue.remove(elem)
#                 if elem-person >= people[-1]:
#                     queue.append(elem-person)
#                     queue.sort
#                 break
#         else:
#             answer += 1
#             if limit - person >= people[-1]:
#                 queue.append(limit-person)
#         print(answer, person, queue)
#     return answer


# sol2. 문제 조건 중 보트에는 최대 두 명만 탑승가능하다는 조건을 확인하고 코드 수정
def solution(people, limit):
    people.sort(reverse=True)
    answer = 0
    for person in people:
        answer += 1
        if limit - person >= people[-1]:
            people.pop()
    return answer

if __name__=="__main__":
    people = [70, 50, 81, 50, 20, 20, 10]
    limit = 100
    print(solution(people,limit))