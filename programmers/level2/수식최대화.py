# https://programmers.co.kr/learn/courses/30/lessons/67257

from itertools import permutations
import copy

def solution(expression):
    input_list = []
    oper_list = []
    answers = []
    k = 0
    for i, char in enumerate(expression):
        if ord(char) < 48 or ord(char) > 57:
            input_list.append(expression[k:i])
            k = i+1
            input_list.append(expression[i])
            oper_list.append(expression[i])
    input_list.append(expression[k:])
    oper_permute = list(permutations(set(oper_list)))
    # print(oper_permute)
    
    for opers in oper_permute:
        input_list_ = copy.deepcopy(input_list)
        print(opers)
        for oper in opers:
            temp = []
            while len(input_list_) > 0:
                poppop = input_list_.pop(0)
                if poppop != oper:
                    temp.append(poppop)
                if poppop == oper:
                    cal = calculate(int(temp.pop()), int(input_list_.pop(0)), poppop)
                    temp.append(cal)
            input_list_ = temp
            print(temp)
        answers.append(abs(input_list_[0]))
        print(answers)

    return max(answers)

def calculate(a,b,oper):
    if oper == "*":
        return a*b
    elif oper == "+":
        return a+b
    elif oper == "-":
        return a-b

if __name__ == "__main__":
    expression = "100-200*300-500+20"
    print(solution(expression))
