# https://programmers.co.kr/learn/courses/30/lessons/42860

def solution(name):
    right = 0
    min_move = len(name) - 1
    while name[min_move] == 'A' and min_move > 0:
        min_move -= 1
        
    for i, char in enumerate(name): 
        updown = ord(char) - ord("A")
        if updown > 13: #down 으로 가는게 빠른 case
            updown = 26 - updown
        right += updown
    
        A_end = i+1
        while A_end < len(name) and name[A_end] == "A":
            A_end +=1

        min_move = min(min_move, 2*i + len(name) - A_end)
            
    right += min_move

    left = 0
    min_move = len(name) - 1

    j = 0
    while j != -len(name):
        updown = ord(name[j]) - ord("A")
        if updown > 13:
            updown = 26- updown
        left += updown
    
        A_end = j-1
        while A_end > -len(name) and name[A_end] == "A":
            A_end -= 1
        min_move = min(min_move, 2*abs(j) +len(name) - A_end)
    
        j -= 1
        
    left += min_move
    
    
    return min(right, left)

if __name__ == "__main__":
    name1 = "JEROEN"
    name2 = "JAN"
    print(solution(name1))