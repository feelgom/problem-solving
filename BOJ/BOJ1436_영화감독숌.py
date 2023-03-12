N = int(input())
count = 0
for i in range(1000000000):
    if "666" in str(i):
        count += 1
    if count == N:
        break
    
print(i)
    