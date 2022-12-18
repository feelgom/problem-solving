string = input().upper()

dic = {}
for char in string:
    if char not in dic:
        dic[char] = 0
    dic[char] +=1
    
max_ = 0 
for key,value in dic.items():
    if value > max_:
        max_ = value
        ans = key
    elif value == max_:
        ans = '?'    
    
print(ans)
