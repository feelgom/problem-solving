# https://programmers.co.kr/learn/courses/30/lessons/42860

def solution(name):
    updown=0
    leftright=9999999
    not_A=[]
    for i,char in enumerate(name):
        temp = ord(char) - ord("A")
        updown+= min(temp, 26-temp)

        if char!='A' or i==0:
            not_A.append(i)
    not_A.append(len(name))

    for i in range(len(not_A)-1):
        right  = not_A[i]
        left = len(name) - not_A[i+1]
        temp = min(right,left)*2 + max(right,left)
        leftright = min(leftright, temp)

    return updown + leftright

if __name__ == "__main__":
    name1 = "JEROEN"
    name2 = "JAN"
    names = ["JEROEN", "JAN", "AAB", 'AAABBBABA', "BBABAAAABBBAAAABABB", "BBAAAAAABBBAAAAAABB"]
    answers = [56, 23, 2, 10, 26,20]
    print(solution(names[5]))