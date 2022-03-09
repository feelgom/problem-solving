# https://programmers.co.kr/learn/courses/30/lessons/17677

def solution(str1, str2):
    intersection = []
    union = []
    
    set1 = str2list(str1)
    set2 = str2list(str2)
    
    for item in set1:
        if item in set2:
            set2.remove(item)
            intersection.append(item)
    
    union = set1 + set2

    if len(union) == 0:
        return 65536
    
    jacad = len(intersection) / len(union)
    answer = int(jacad * 65536)
    return answer


def str2list(string):
    ans = []
    for i in range(len(string)-1):
        asci = ord(string[i])
        if (asci >= 65 and asci <= 90) or ( asci >= 97 and asci <= 122 ):
            if ( asci >= 97 and asci <= 122 ):
                asci = asci - 32
            asci2 = ord(string[i+1])
            if (asci2 >= 65 and asci2 <= 90) or ( asci2 >= 97 and asci2 <= 122 ):
                if (asci2 >= 97 and asci2 <= 122):
                    asci2 = asci2 - 32    
                ans.append(chr(asci)+chr(asci2))
                
    return ans
    
    
if __name__ == "__main__":
    str1 = "FRANCE"
    str2 = "french"

    print(solution(str1,str2))

    
