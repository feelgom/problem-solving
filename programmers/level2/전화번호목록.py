# https://programmers.co.kr/learn/courses/30/lessons/42577

def solution(phone_book):
    answer = True
    
    dictionary = [{},0]
    
    for phone_number in phone_book:
        dict_ = dictionary
        for number in phone_number:
            if not number in dict_[0]:
                dict_[0][number] = [{}, 0]
                
            if dict_[0][number][1] == 1:
                return False
            
            dict_ = dict_[0][number]
            
        if len(dict_[0]) != 0:
            return False
            
        dict_[1] = 1

    return answer

if __name__ == "__main__":
    # phone_book = ["119", "97674223", "1195524421"]
    phone_book = ['1','2','4']
    print(solution(phone_book))
