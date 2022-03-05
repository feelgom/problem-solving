def solution(record):
    log = {}
    for code in record:
        codes = code.split(' ')
        if codes[0] == 'Enter':
            log[codes[1]] = codes[2]
        if codes[0] == 'Change':
            log[codes[1]] = codes[2]
    
    result = []
    for code in record:
        codes = code.split(' ')
        if codes[0] == 'Enter':
            result.append(log[codes[1]]+"님이 들어왔습니다.")
        if codes[0] == 'Leave':
            result.append(log[codes[1]]+"님이 나갔습니다.")
    
    return result
    

if __name__ == "__main__":
    record = ["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]
    print(solution(record))
