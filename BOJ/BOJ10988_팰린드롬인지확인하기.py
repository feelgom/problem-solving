string = input()

for i in range(len(string)):
    if string[i] != string[-1-i]:
        print(0)
        break
else:
    print(1)
    