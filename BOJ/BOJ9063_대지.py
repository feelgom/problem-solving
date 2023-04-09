N = int(input())
x_max = -9999999
x_min = 9999999
y_max = -9999999
y_min = 9999999
    
for _ in range(N):
    x,y, = map(int, input().split())
    if x > x_max:
        x_max = x
    if x < x_min:
        x_min = x
    if y > y_max:
        y_max = y
    if y < y_min:
        y_min = y
    
print((x_max-x_min)*(y_max-y_min))
