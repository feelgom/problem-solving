N = int(input())

for i in range(N):
    string = " " * (N-1-i) + "*" * (2*i+1)
    print(string)
    
for j in range(N-1):
    i = N-2-j
    string = " " * (N-1-i) + "*" * (2*i+1)
    print(string)