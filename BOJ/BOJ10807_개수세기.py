_ = input()
inputs = list(map(int,input().split()))

list_ = [0]*300
for i in inputs:
    list_[i]+=1
    
query = int(input())
print(list_[query])