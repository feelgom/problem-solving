N = int(input())
nums = []
for _ in range(N):
    nums.append(int(input()))

nums.sort()
for elem in nums:
    print(elem)