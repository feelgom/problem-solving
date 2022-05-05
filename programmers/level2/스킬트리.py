# https://programmers.co.kr/learn/courses/30/lessons/49993

def solution(skill, skill_trees):
    answer =0   
    for test in skill_trees:
        ll = []
        for sk in skill:
            temp = test.find(sk)
            if temp == -1:
                ll.append(9999999999)
            else:
                ll.append(temp)

        rr = ll.copy()
        rr.sort(reverse=False)

        if ll==rr:
            answer += 1
    
    return answer

if __name__=="__main__":
    skill = "CBD"   
    skill_trees = ["BACDE", "CBADF", "AECB", "BDA", "CB"]
    answer = 2
    
    print(solution(skill,skill_trees)==answer, solution(skill,skill_trees))