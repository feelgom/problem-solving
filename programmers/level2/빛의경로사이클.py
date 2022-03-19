# https://programmers.co.kr/learn/courses/30/lessons/86052

import numpy as np
def solution(grid):
    answer = []

    array = np.zeros([len(grid),len(grid[0]),4])
    # 0:위, 1:오른, 2:아래, 3:왼

    d_dict = {
        0: [0,-1],
        1: [1,0],
        2: [0,1],
        3: [-1,0]
    }
    turn_dict = {
        'S': 0,
        'R': 1,
        'L': -1
    }


    for x in range(array.shape[0]):
        for y in range(array.shape[1]):
            for d in range(4):
                count = 0
                while array[x][y][d] == 0:
                    array[x][y][d] = 1
                    count += 1

                    dx, dy = d_dict[d]
                    x += dx
                    x = x % array.shape[0]
                    y += dy
                    y = y % array.shape[1]
                    d += turn_dict[grid[x][y]]
                    d = d % 4

                if count > 0:
                    answer.append(count)

    answer.sort(reverse=True)
    return answer


if __name__ == "__main__":
    grid1 = ["SL","LR"]
    grid2 = ["S"]
    grid3 = ["R","R"]
    print(solution(grid1))
    print(solution(grid2))
    print(solution(grid3))