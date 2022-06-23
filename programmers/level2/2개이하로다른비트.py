# https://programmers.co.kr/learn/courses/30/lessons/77885

def solution(numbers):
    answer = []
    for i in numbers:
        i_bin = bin(i)[2:]
        i_list = list(i_bin)

        if i_list[-1] == "0":
            i_list[-1] = "1"
        else:
            for idx in range(2, len(i_list)+1):
                if i_list[-idx] == "0":
                    i_list[-idx] = "1"
                    i_list[-idx+1] = "0"
                    break
            else:
                i_list = ["1", "0"] + i_list[1:]
        
        new = "".join(i_list)
        answer.append(int("0b"+new,2))

    return answer