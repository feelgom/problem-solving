# https://programmers.co.kr/learn/courses/30/lessons/42587

def solution(priorities, location):
    answer = 0
    
    i = 0
    while True:
        if priorities[i%len(priorities)] == max(priorities):
            priorities[i%len(priorities)] = 0
            answer += 1
            if i%len(priorities) == location:
                break
        
        i += 1
    
    return answer

if __name__ == "__main__":
    priorities = [2, 1, 3, 2]
    location = 2
    print(solution(priorities, location))