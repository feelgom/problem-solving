
def solution(fees, records):
    queue = {}
    pay = {}
    for record in records:
        time, number, inout = record.split(' ')
        minu, sec = time.split(':')
        sec += minu*60
        if number not in pay:
            pay[number] = 0

        if number not in queue:
            queue[number] = sec
        else:
            pay[number] += fees[1]
            pay_time = (sec - queue[number])
            if pay_time > fees[0]:
                pay[number] += (pay_time - fees[0])/fees[2]*fees[3]
            



    return 0

if __name__=="__main__":
    fees = [180, 5000, 10, 600]
    records = ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]
    results = [14600, 34400, 5000]
    print(solution(fees,records) == results)
    print(solution(fees,records))
