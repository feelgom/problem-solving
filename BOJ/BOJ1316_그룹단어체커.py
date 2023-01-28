N = int(input())

ans = 0
for _ in range(N):
    char_set = []
    string = input()
    prev = ""
    for char in string:
        if char == prev:
            continue
        else:
            prev = char
            
        if char not in char_set:
            char_set.append(char)
        else:
            break
    else:
        ans+=1
        
print(ans)