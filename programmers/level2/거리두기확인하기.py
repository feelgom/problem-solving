dic = [[1,0],[-1,0],[0,1],[0,-1]]


def solution(places):
    result = []
    for place in places:
        flag = 1
        for x in range(5):
            for y in range(5):
                if place[x][y] == 'P': 
                    for i in range(4):
                        dx, dy = dic[i]
                        nx = x + dx
                        ny = y + dy
                        if nx < 0 or nx >= 5 or ny < 0 or ny >= 5:
                            continue
                        if place[nx][ny] =="P":
                            flag = 0
                            break
                        elif place[nx][ny] == "O":
                            count = 0
                            for j in range(4):
                                dxx, dyy = dic[j]
                                nxx = nx+dxx
                                nyy = ny+dyy
                                if nxx<0 or nxx>=5 or nyy<0 or nyy>=5:
                                    continue
                                if place[nxx][nyy] =="P":
                                  count += 1
                            if count >= 2:
                                flag = 0
                                break
                if flag == 0:
                    break
            if flag == 0:
                result.append(0)
                break
        if flag ==1:
            result.append(1)
                
    return result

if __name__ == "__main__":
    places = [["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]
    print(solution(places))
