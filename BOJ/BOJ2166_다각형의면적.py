def triangle_area(A,B,C):
    area = abs(A[0]*B[1]+B[0]*C[1]+C[0]*A[1]-(A[1]*B[0]+B[1]*C[0]+C[1]*A[0]))/2
    return area

N = int(input())
points = []
for _ in range(N):
    points.append(list(map(int,input().split())))

ans = 0
for i in range(N):
    ans += points[i][0] * points[i-1][1]
    ans -= points[i][1] * points[i-1][0]
ans = abs(ans)/2
    
print(round(ans,1))