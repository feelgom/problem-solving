T = int(input())
for _ in range(T):
    C = int(input())
    quarter = C//25
    C %= 25
    
    dime = C//10
    C %= 10
    
    nikel = C//5
    C%= 5
    
    penny = C
    
    print(quarter, dime, nikel, penny)