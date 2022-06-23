# https://programmers.co.kr/learn/courses/30/lessons/87377

def solution(line):
    points = []
    for i in range(len(line)-1):
        for j in range(i+1, len(line)):
            a,b,e = line[i]
            c,d,f = line[j]
            
            if a*d-b*c == 0:
                continue
            else:
                x = (b*f-e*d)/(a*d-b*c)
                y = (e*c-a*f)/(a*d-b*c)
                if int(x) - x == 0 and int(y) - y == 0:
                    points.append([int(x),int(y)])
                  
    x_max = max(points, key=lambda x:x[0])[0]
    x_min = min(points, key=lambda x:x[0])[0]
    y_max = max(points, key=lambda x:x[1])[1]
    y_min = min(points, key=lambda x:x[1])[1]
    
    result = ["."*(x_max-x_min+1)] * (y_max-y_min+1)
    result = [list(elem) for elem in result]

    for x,y in points:
        result[y_max-y][x-x_min] = "*"

    answer = []
    for elem in result:
        answer.append("".join(elem))
    
    return answer