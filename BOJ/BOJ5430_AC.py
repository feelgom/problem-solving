from collections import deque

T=int(input())
for _ in range(T):
    actions = input()
    N=int(input())
    queue = deque(input()[1:-1].split(","))
    
    reverse = False
    for act in actions:
        if act == "R":
            reverse = not reverse
        elif act == "D" and N>0:
            if reverse:
                queue.pop()
            else:
                queue.popleft()
            N-=1
        else:
            print("error")
            break
    else:
        if reverse:
            queue.reverse()
        print("[", ",".join(queue), "]", sep="")
    