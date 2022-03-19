# https://programmers.co.kr/learn/courses/30/lessons/42839

import math
from itertools import permutations

def solution(numbers):
    numbers_list = list(numbers)
    answer = 0
    candidates = []
    for length in range(1, len(numbers)+1):
        permute_set = set(permutations(numbers_list, length))
        permute_list = list(permute_set)
        for num_list in permute_list:
            temp = ''
            for num in num_list:
                temp = temp + num
            candidates.append(int(temp))

    candidates = list(set(candidates))

    for item in candidates:
        if is_prime_number(item) == True:
            answer += 1

    return answer


def is_prime_number(x):
    if x <= 1:
        return False
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False 
    return True

if __name__ == "__main__":
    numbers = "17"
    print(solution(numbers))