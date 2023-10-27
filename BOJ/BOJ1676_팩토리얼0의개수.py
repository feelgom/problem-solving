import math
N = int(input())

fact = str(math.factorial(N))
for i, char in enumerate(fact[::-1]):
    if char != "0":
        print(i) 
        break
