import sys
import time
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def main(N, nums):
    results = [0]*1000001
    exists = [False]*1000001
    for i in nums: # O(N) 100000
        exists[i] = True
    
    for i in nums: # O(N) 100000
        for j in range(i*2, 1000001, i):
            if exists[j]:
                results[i] += 1
                results[j] -= 1
    
    ans = [results[i] for i in nums]
                
    print(*ans)

if __name__ == "__main__":
    start = time.time()
    
    N=int(input())
    nums = list(map(int,input().split()))
    # N = 100000
    # nums = [i*10 for i in range(1, N+1)]
    main(N, nums)
    # print(f"{time.time() - start:.5f} sec")