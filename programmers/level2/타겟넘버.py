# https://programmers.co.kr/learn/courses/30/lessons/43165

def solution(numbers, target):
    count = 0
    numbers.sort(reverse=True)
    newTarget = sum(numbers) - target
    return DFS(numbers, newTarget, count)
        
        
def DFS(array, newTarget, count):
    if len(array) == 0:
        return count

    if 2 * array[0] == newTarget:
        count += 1

    if 2 * array[0] < newTarget:
        count = DFS(array[1:], newTarget - 2 * array[0], count)

    count = DFS(array[1:], newTarget, count)
    
    return count 

if __name__ == "__main__":
    aa = [4, 1, 2, 1]
    print(solution(aa, 4))