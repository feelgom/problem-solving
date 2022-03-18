# https://programmers.co.kr/learn/courses/30/lessons/42746

def solution(numbers):
    newList = []    
    for number in numbers:
        num_str = str(number)
        num_str = num_str + num_str[0] * (4-len(num_str))
        if int(num_str[0])>int(num_str[1]):
            num_int = int(num_str) - (4-len(str(number)))*0.1
        else:
            num_int = int(num_str) + (4-len(str(number)))*0.1

        newList.append(num_int)

    # newList.sort(reverse=True)
    sorted_index = sorted(range(len(newList)), key=lambda k: newList[k], reverse=True)
    print(newList)
    print(sorted_index)

    answer = ""
    for index in sorted_index:
        answer = answer + str(numbers[index])

    return str(int(answer))

if __name__ == "__main__":
    numbers = [0,0,0,0]
    print(solution(numbers))
