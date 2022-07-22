# https://school.programmers.co.kr/learn/courses/30/lessons/92341

from math import ceil
def solution(fees, records):
    queue = {}
    times = {}
    pay = {}
    for record in records:
        time, number, inout = record.split(' ')
        hour, minute = map(int,time.split(':'))
        minute += hour*60

        if number not in pay:
            pay[number] = 0
        if number not in times:
            times[number] = 0

        if inout == "IN":
            queue[number] = minute
        elif inout == "OUT":
            times[number] += minute - queue[number]
            queue.pop(number)

    for number, time in queue.items():
        times[number] += 23*60+59 - time

    keys = list(times.keys())
    keys.sort()
    
    for key in keys:
        pay[key] += fees[1]
        if times[key] > fees[0]:
            pay[key] +=  ceil((times[key] - fees[0])/fees[2]) *fees[3]

    answer = [int(pay[key]) for key in keys]

    return answer

if __name__=="__main__":
    fees = [180, 5000, 10, 600]
    records = ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]
    results = [14600, 34400, 5000]
    print(solution(fees,records))
    print(solution(fees,records) == results)
