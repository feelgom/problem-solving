# https://programmers.co.kr/learn/courses/30/lessons/76502

def solution(s):
    left ={"(":0,"{":1,"[":2}
    right ={")":0,"}":1,"]":2}

    for i in range(len(s)):
        new_s = s[i:]+s[0:i]
        
        stack = []
        count = 0
        finish = True
        for char in new_s:
            if char in left:
                stack.append(char)
            elif char in right:
                if len(stack) == 0:
                    finish = False
                    break
                
                stack_pop = stack.pop(-1)
                if left[stack_pop] == right[char]:
                    if len(stack) == 0:
                        count += 1
                else:
                    finish = False
                    break

        if finish:    
            return count
            
    return 0

if __name__=="__main__":
    ss = ["[](){}", "}]()[{", "[)(]", "}}}"]
    results = [3,2,0,0]
    for i in range(len(ss)):
        print( solution(ss[i]) == results[i],  solution(ss[i]))