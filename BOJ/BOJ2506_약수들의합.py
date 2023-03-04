while True:
    N = int(input())
    if N == -1:
        break
    count = 0
    lis = []
    for i in range(1,N):
        if N%i ==0:
            count += i
            lis.append(str(i))
    if count == N:
        string = " + ".join(lis)
        print(f"{N} = {string}")
    else:
        print(f"{N} is NOT perfect.")
        