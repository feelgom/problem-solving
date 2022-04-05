# https://programmers.co.kr/learn/courses/30/lessons/42583

def solution(bridge_length, weight, truck_weights):
    answer = 0
    queue = [0] * bridge_length
    while(len(truck_weights) != 0):
        answer += 1
        queue.pop(0)
        if sum(queue) + truck_weights[0] <= weight:
            queue.append(truck_weights.pop(0))
        else:
            queue.append(0)
        
    answer += bridge_length
          
    return answer

if __name__ == "__main__":
    bridge_length = 2
    weight = 10
    truck_weights = [7,4,5,6]
    print(solution(bridge_length, weight, truck_weights))