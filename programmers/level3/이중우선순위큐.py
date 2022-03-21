# https://programmers.co.kr/learn/courses/30/lessons/42628

import heapq
def solution(operations):
    minheap = []
    maxheap = []

    for operation in operations:
        oper, data = operation.split(' ')
        if oper == "I":
            heapq.heappush(minheap, int(data))
            heapq.heappush(maxheap, (-int(data), int(data)))

        else:
            if len(minheap) == 0:
                continue

            if data == "1":
                val = heapq.heappop(maxheap)[1]
                minheap.remove(val)

            elif data == "-1":
                val = heapq.heappop(minheap)
                maxheap.remove((-val,val))

    if len(minheap) == 0:
        return [0,0]

    else:
        return [heapq.heappop(maxheap)[1], heapq.heappop(minheap)]

if __name__ == "__main__":
    operations = ["I 16","D 1"]
    operations2 = ["I 7","I 5","I -5","D -1"]
    print(solution(operations2))
