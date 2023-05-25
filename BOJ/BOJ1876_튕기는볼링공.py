import math

N = int(input())
for _ in range(N):
    T, degree = map(float,input().split())
    a =  math.tan(math.radians(degree))
    pin_x = T * 100
    Y = a * pin_x
    pin_y = round(Y/85) * 85
    # y = a * x
    # 점과 직선사이 거리
    # d = abs(ax0 + by0 + c) / math.sqrt(a**2 + b**2)
    d = abs(a*pin_x - pin_y) / math.sqrt(a**2 + 1)
    if d <= 16:
        print('yes')
    else:
        print('no')
    