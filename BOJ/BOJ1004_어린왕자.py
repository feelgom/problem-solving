def is_inside(x,y,cx,cy,r):
    if (x-cx)**2+(y-cy)**2 < r**2:
        return True
    else:
        return False

T = int(input())
for _ in range(T):
    ans = 0
    x1,y1,x2,y2 = map(int,input().split())
    n = int(input())
    for _ in range(n):
        cx,cy,r = map(int,input().split())
        if is_inside(x1,y1,cx,cy,r) != is_inside(x2,y2,cx,cy,r):
            ans+=1
            
    print(ans)
