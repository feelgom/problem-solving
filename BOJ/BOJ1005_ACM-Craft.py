from collections import deque
import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N, K = map(int,input().split())
    build_times = [0] + list(map(int,input().split()))
    build_times_sum = build_times[:]
    
    orders = {i:[] for i in range(1,N+1)}
    counts = [0]*(N+1)
    for _ in range(K):
        a, b = map(int,input().split())
        orders[a].append(b)
        counts[b] += 1
        
    W = int(input())
    queue = deque([i for i in range(1,N+1) if counts[i] == 0])
    while queue:
        end_flag = False
        pre = queue.popleft()
        for post in orders[pre]:
            counts[post] -= 1
            if build_times_sum[pre] + build_times[post] > build_times_sum[post]:
                build_times_sum[post] = build_times_sum[pre] + build_times[post]    
            if counts[post] == 0:
                if post == W:
                    end_flag = True
                    break
                queue.append(post)
        if end_flag:
            break

    print(build_times_sum[W])