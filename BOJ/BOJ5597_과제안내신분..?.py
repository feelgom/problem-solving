lis = []
for _ in range(28):
    lis.append(int(input()))

for i in range(1,31):
    if i not in lis:
        print(i)