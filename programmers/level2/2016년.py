# https://programmers.co.kr/learn/courses/30/lessons/12901

def solution(a, b):
    day = ["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"] 
    dates_per_month = [0, 31,29,31,30,31,30,31,31,30,31,30,31]
    days = sum(dates_per_month[:a]) + b
    
    return day[(days+4)%7]

if __name__=="__main__":
    a,b = 5,24
    answer = "TUE"
    print(solution(a,b)==answer, solution(a,b))