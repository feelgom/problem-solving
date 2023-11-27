from collections import deque
S = input().rstrip()
T = deque(input().rstrip())

reverse = False
while len(T) > len(S):
    if not reverse:
        pop = T.pop()
        if pop == 'B':
            reverse = not reverse
    else:
        pop = T.popleft()
        if pop == 'B':
            reverse = not reverse
    
    # print(T)
    
if reverse:
    T.reverse()
if ''.join(T) == S:
    print(1)
else:
    print(0)
