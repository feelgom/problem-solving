# https://programmers.co.kr/learn/courses/30/lessons/42860

def solution(name):
    compare1 = ["A"]*len(name)
    compare2 = ["A"]*len(name)
    answer = 0
    right = 0
    left = 0
    for i, char in enumerate(name): 
        updown = ord(char) - 65
        if updown > 13: #down 으로 가는게 빠른 case
            updown = 26 - updown
        right += updown
        compare1[i] = char
        if "".join(compare1) == name:
            break
        else:
            right += 1
    
    j = 0
    while j != -len(name):
        updown = ord(name[j]) - 65
        if updown > 13:
            updown = 26- updown
        left += updown
        compare2[j] = name[j]
        if "".join(compare2) == name:
            break
        else:
            left +=1
            j -= 1
    print(right, left)
    return min(right, left)

if __name__ == "__main__":
    name1 = "JEROEN"
    name2 = "JAN"
    print(solution(name1))