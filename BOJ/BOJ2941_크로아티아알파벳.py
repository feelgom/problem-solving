cro = ["c=","c-","dz=","d-","lj","nj","s=","z="]

string = input()
start = 0
ans = 0
while start<len(string):
    if string[start:start+2] in cro:
        start +=2
    elif string[start:start+3] in cro:
        start += 3
    else:
        start += 1
    ans += 1

print(ans)