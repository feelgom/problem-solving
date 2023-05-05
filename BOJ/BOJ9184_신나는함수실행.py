dic = {}
def reg(a,b,c):
    if (a,b,c) in dic:
        return dic[(a,b,c)]
    if a <= 0 or b <= 0 or c <= 0:
        dic[(a,b,c)] = 1
    elif a > 20 or b > 20 or c > 20:
        dic[(a,b,c)] = reg(20,20,20)
    elif a < b and b < c:
        dic[(a,b,c)] = reg(a,b,c-1)+reg(a,b-1,c-1)-reg(a,b-1,c)
    else:
        dic[(a,b,c)] = reg(a-1,b,c)+reg(a-1,b-1,c)+reg(a-1,b,c-1)-reg(a-1,b-1,c-1)

    return dic[(a,b,c)]
    
while 1:
    a, b, c = map(int,input().split())
    if a == b == c == -1:
        break
    ans = reg(a,b,c)
    print(f"w({a}, {b}, {c}) = {ans}")
    