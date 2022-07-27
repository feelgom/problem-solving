# https://school.programmers.co.kr/learn/courses/30/lessons/1845

def solution(nums):
    nums_set = set(nums)
    return min(len(nums)/2, len(nums_set))