x1,y1 = map(int,input().split())
x2,y2 = map(int,input().split())
x3,y3 = map(int,input().split())

vec1 = [x2-x1, y2-y1, 0]
vec2 = [x3-x2, y3-y2, 0]

cross = vec1[0]*vec2[1] - vec1[1]*vec2[0]
if cross > 0:
    print(1)
elif cross == 0:
    print(0)
else:
    print(-1)
