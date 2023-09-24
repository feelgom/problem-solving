x1,y1,x2,y2 = map(int,input().split())
x3,y3,x4,y4 = map(int,input().split())

# 직선1 (y2-y1)/(x2-x1) * (x - x1) - (y - y1) = 0
# 직선2 (y4-y3)/(x4-x3) * (x - x3) - (y - y3) = 0
val1 = (y4-y3)/(x4-x3+1E-10) * (x1 - x3) - (y1 - y3)
val2 = (y4-y3)/(x4-x3+1E-10) * (x2 - x3) - (y2 - y3)

val3 = (y2-y1)/(x2-x1+1E-10) * (x3 - x1) - (y3 - y1)
val4 = (y2-y1)/(x2-x1+1E-10) * (x4 - x1) - (y4 - y1)

if val1*val2 < 0 and val3*val4 < 0:
    print(1)
else:
    print(0)