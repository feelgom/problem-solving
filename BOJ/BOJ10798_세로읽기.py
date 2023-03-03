lis = []
max_length = 0
ans =""

for _ in range(5):
    string = input()
    if len(string) > max_length:
        max_length = len(string)
    lis.append(string)
    
for i in range(max_length):
    for string in lis:
        if i < len(string):
            ans += string[i]
    
print(ans)
