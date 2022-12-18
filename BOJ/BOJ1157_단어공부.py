string = input().lower()

dic = {}
for char in string:
    if char not in dic:
        dic[char] = 0
    dic[char] +=1
    
ans = "?"
max_ = 0 
for key,value in dic.items():
    if value > max_:
        max_ = value
        ans = key
        
print(ans)
