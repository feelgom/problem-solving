while True:
    A,B,C = map(int, input().split())
    if A == 0 and B == 0 and C == 0:
        break
    elif A == B and A == C:
        print("Equilateral")
    elif  max(A,B,C) < A+B+C - max(A,B,C):
        if A == B or B == C or C == A:
            print("Isosceles")
        else:
            print("Scalene")
    else:
        print("Invalid")