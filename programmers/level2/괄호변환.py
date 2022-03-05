def reverse(u):
    reverse_ = []
    for char in u:
        if char == "(":
            reverse_.append(")")
        elif char == ")":
            reverse_.append("(")
        else:
            raise
    return reverse_

def checkRight(u):
    left = 0
    right = 0
    for char in u:
        if char == "(":
            left += 1
        elif char == ")":
            right += 1
        # else:
            # raise
        
        if right > left:
            return 1
        
        if left == right:
            return 0
    raise

def solution(p):
    if p == "":
        return p
    u = []
    v = []
    left = 0
    right = 0
    for char in p:
        if left == right and left != 0:
            v.append(char)
            continue
            
        u.append(char)
        if char == "(":
            left += 1
        elif char == ")":
            right += 1
        else:
            raise
    
    if checkRight(u) == 0:
        vAnswer = solution("".join(v))
        answer = "".join(u) + vAnswer
        
    elif checkRight(u) == 1:
        
        vAnswer = solution("".join(v))
        uReverse = reverse(u[1:-1])
        answer = "(" + vAnswer + ")" + "".join(uReverse)
        
        print(answer)
    return answer


if __name__ == "__main__":
    p = "()))((()"
    print(solution(p))