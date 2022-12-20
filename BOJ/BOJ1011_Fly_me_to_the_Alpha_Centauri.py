
def solution(x,y):
    distance = y-x
    

if __name__ == "__main__":
    T = 3
    arr = [[0, 3],
    [1, 5],
    [45, 50]]
    ans = [3,3,4]
    for i in range(T):
        x,y = arr[i]
        print(solution(x,y) == ans[i], solution(x,y))