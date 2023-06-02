def point_square_distance(p1,p2):
    return (p1[0]-p2[0])**2 + (p1[1]-p2[1])**2

T = int(input())
for _ in range(T):
    is_square = True
    points = []
    for _ in range(4):
        point = list(map(int,input().split()))
        points.append(point)
        
    distances = []
    for i in range(4):
        for j in range(i+1,4):
            square_distance = point_square_distance(points[i], points[j])
            distances.append(square_distance)
    
    distances.sort()
    if distances[0] != distances[1] or distances[1] != distances[2] or distances[2] != distances[3]:
        is_square = False
    elif distances[4] != distances[5]:
        is_square = False
    elif distances[4] != 2*distances[0]:
        is_square = False
    
    if is_square:
        print(1)
    else:
        print(0)