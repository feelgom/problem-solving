N=int(input())
for _ in range(N):
    string = input()
    if len(string) < 11:
        print(string)
    else:
        print(string[0] + str(len(string)-2) + string[-1])