N = int(input())
buildings = list(map(int,input().split()))

ans = 0
for i in range(N):
    # print("\ni: ", i)
    count = 0
    # 오른쪽으로
    gradient_max = -9999999999999999
    # print("오른쪽으로")
    for j in range(i+1,N):
        # print("j: ",j)
        gradient = (buildings[j]-buildings[i]) / (j-i)
        if gradient > gradient_max:
            gradient_max = gradient
            count += 1
    
    # 왼쪽으로
    gradient_min = 9999999999999999
    # print("왼쪽으로")
    for j in range(i):
        # print("j: ",j)
        gradient = (buildings[i]-buildings[i-1-j]) / (+1+j)
        if gradient < gradient_min:
            gradient_min = gradient
            count += 1
    
    if count > ans:
        ans = count
print(ans)