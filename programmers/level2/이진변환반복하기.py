# https://programmers.co.kr/learn/courses/30/lessons/70129

def solution(s):
    zeros = 0 
    count = 0 
    
    i =0
    while s != '1':
        i+=1
        count+=1
        s_list = [int(x) for x in s]
        new_length = sum(s_list)
        zeros += len(s) - new_length
        temp = []
        while new_length >= 1:
            temp.append(str(new_length%2))
            new_length = new_length // 2
        
        temp.reverse()
        s = "".join(temp)
            
    return [count, zeros]

if __name__=="__main__":
    s = "1111111"
    print(solution(s))