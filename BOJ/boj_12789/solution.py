N = int(input())
students = list(map(int, input().split()))
students.append(N+1)

stack = [0]
call = 1
for student in students:
    while stack[-1] == call:
        call += 1
        stack.pop()
        
    if student == call:
        call += 1
    else:
        stack.append(student)
        
if len(stack) == 1 and stack[0] == 0:
    print("Nice")
else:
    print("Sad")
        