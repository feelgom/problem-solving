N,K = map(int,input().split())
lines = []
for _ in range(N):
    lines.append(int(input()))
    
maximum = sum(lines) // K

def binary_search(start, end):
    mid = (start + end) // 2
    count = 0
    for line in lines:
        count += line // mid
    if count >= K:
        if start == mid:
            return mid
        return binary_search(mid, end)
    else:
        return binary_search(start, mid)
    
print(binary_search(1, maximum+1))