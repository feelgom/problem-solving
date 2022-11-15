#%%
import sys
N = int(input())

r_sum, g_sum, b_sum = 0,0,0
for _ in range(N):
    r,g,b = map(int,sys.stdin.readline().strip().split())
    
    r_temp = r + min(g_sum, b_sum)
    g_temp = g + min(r_sum, b_sum)
    b_temp = b + min(r_sum, g_sum)
    r_sum = r_temp
    g_sum = g_temp
    b_sum = b_temp
    
print(min(min(r_sum,g_sum),b_sum))