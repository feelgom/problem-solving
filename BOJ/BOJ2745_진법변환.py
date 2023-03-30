string, base = input().split()

result = 0
for i, char in enumerate(string[::-1]):
    if char.isdigit():
        result += int(char) * (int(base) ** i)
    else:
        result += (ord(char) - 55) * (int(base) ** i)
        
print(result)