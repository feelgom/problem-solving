# https://programmers.co.kr/learn/courses/30/lessons/77485

def solution(rows, columns, queries):
    answer_total = []
    maps = [ [columns * j + i for i in range(columns+1)] for j in range (-1, rows)]
    
    for query in queries:
        answer = []
        x1, y1, x2, y2 = query
        answer.append(maps[x1][y1])
        for x in range(x1+1,x2+1):
            answer.append(maps[x][y1])
            maps[x-1][y1] = maps[x][y1]
        for y in range(y1+1,y2+1):
            answer.append(maps[x2][y])
            maps[x2][y-1] = maps[x2][y]
        for i in range(x2-x1):
            x = x2-1-i
            answer.append(maps[x][y2])
            maps[x+1][y2] = maps[x][y2]
        for i in range(y2-y1):
            y = y2-1-i
            answer.append(maps[x1][y])
            maps[x1][y+1] = maps[x1][y]
        maps[x1][y1+1] = answer[0]
        
        answer_total.append(min(answer))
    
    return answer_total


if __name__ == "__main__":

    i = 0
    rows = [6, 3, 100]
    columns = [6, 3, 97]
    queries = [
        [[2,2,5,4],[3,3,6,6],[5,1,6,3]],
        [[1,1,2,2],[1,2,2,3],[2,1,3,2],[2,2,3,3]],
        [[1,1,100,97]]
    ]
    print(solution(rows[i], columns[i], queries[i]))