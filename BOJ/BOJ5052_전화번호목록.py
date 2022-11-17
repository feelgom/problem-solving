#%%
import sys

def test(numbers):
    numbers.sort()
    for i in range(len(numbers)-1):
        if numbers[i] == numbers[i+1][:len(numbers[i])]:
            print("NO")
            return
    print("YES")
    return
    
if __name__=="__main__":
    T = int(sys.stdin.readline().strip())
    for _ in range(T):
        n = int(sys.stdin.readline().strip())
        numbers = []
        for _ in range(n):
            num = sys.stdin.readline().strip()
            numbers.append(num)
        test(numbers)