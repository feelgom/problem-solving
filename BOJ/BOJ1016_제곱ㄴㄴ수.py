def test(min_num, max_num):
    cands = [True]*(max_num+1 - min_num)
    m = int(max_num ** 0.5)
    for i in range(2, m+1):
        start = (min_num-1) // (i**2) + 1
        end = (max_num) // (i**2)
        for j in range(start, end+1):
            index = ((i**2) * j) - min_num
            if index < len(cands):
                cands[index] = False
        
    return sum(cands)
    
    
if __name__=="__main__":
    a, b = map(int,input().split())
    print(test(a,b))
    
