#BOJ1918_후위표기식.py
string = input()
ans = ""
stack = []
for c in string:
    if c.isalpha():
        ans += c
    else:
        if c == '(':
            stack.append(c)
        elif c == '*' or c =='/':
            while stack and stack[-1] in ['*', '/']:
                ans += stack.pop()
            stack.append(c)
        elif c == "+" or c == "-":
            while stack and stack[-1] not in ["("]:
                ans += stack.pop()
            stack.append(c)
        elif c == ')':
            while stack and stack[-1] != "(":
                ans += stack.pop()
            stack.pop()
    
while stack:
    ans += stack.pop()
print(ans)