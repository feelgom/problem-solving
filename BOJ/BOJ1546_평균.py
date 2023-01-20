N = int(input())
num_list = list(map(int,input().split()))

print(sum(num_list)/ N / max(num_list) * 100)