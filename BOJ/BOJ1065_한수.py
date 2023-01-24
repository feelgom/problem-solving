hansu = [0]*1001

for i in range(1,1001):
    is_hansu = True
    str_i = str(i)

    if len(str_i) > 1:
        dis = int(str_i[1]) - int(str_i[0])
        for ind in range(len(str_i)-1):
            if int(str_i[ind+1]) - int(str_i[ind]) != dis:
                is_hansu = False
                break
    if is_hansu:
        hansu[i] = 1

N = int(input())
print(sum(hansu[:N+1]))