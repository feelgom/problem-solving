N = int(input())
lst = list()
for _ in range(N):
    lst.append(int(input()))

stack = list()
#N = 8   
#lst = list((4,3,6,8,7,5,2,1))
#print(lst)

ans = list()
for num in range(1,N+1):
    while num > lst[0]:
        if stack[-1] == lst[0]:
            lst.pop(0)
            stack.pop()
            ans.append("-")
        else:
            print("NO")
            break

    if num <= lst[0]:
        stack.append(num)
        ans.append("+")
else:
    for elem in ans:
        print(elem)
    for _ in stack:
        print("-")

