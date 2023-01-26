dic = {}
for i in range(26):
    char = chr(i+65)
    if i < 18:
        value = i//3 + 3
    elif i == 18:
        value = 8
    elif i < 22:
        value = 9
    elif i <26:
        value = 10
    dic[char] = value

string = list(input())
ans = 0
for c in string:
    ans += dic[c] 
print(ans)