# https://programmers.co.kr/learn/courses/30/lessons/17686

def solution(files):
    heads = []
    for file in files:
        number_start = None
        number_end = -1
        for i in range(len(file)):
            if (ord(file[i])<48 or ord(file[i])>57) and number_start != None:
                number_end = i
                break
            elif ord(file[i])>=48 and ord(file[i])<=57 and number_start == None:
                number_start = i


        HEAD = file[:number_start].upper()
        if number_end != -1:
            NUMBER = int(file[number_start:number_end])
        else:
            NUMBER = int(file[number_start:])
        heads.append([HEAD, NUMBER, file])

    heads_sort = sorted(heads, key = lambda x : (x[0], x[1]))

    answer = []
    for elem in heads_sort:
        print(elem)
        answer.append(elem[2])
        
    return answer

if __name__=="__main__":
    files =  ["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"]
    # files = ["F-5 Freedom Fighter", "B-50 Superfortress", "A-10 Thunderbolt II", "F-14 Tomcat"]
    print(solution(files))