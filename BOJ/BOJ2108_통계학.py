import sys
input = sys.stdin.readline

N = int(input())
lis = []
counts = [0] * 8001
for _ in range(N):
    num = int(input())
    lis.append(num)
    counts[num] += 1
        
lis.sort()
mean = round(sum(lis)/len(lis))
median = lis[N//2]

range_ = lis[-1]-lis[0]
max_count = max(counts)
mode = counts.index(max_count)
if mode > 4000:
    mode -= 8001
    
counts[mode] = 0
if max_count in counts:
    mode = counts.index(max_count)
if mode > 4000:
    mode -= 8001

print(mean)
print(median)
print(mode)
print(range_)
