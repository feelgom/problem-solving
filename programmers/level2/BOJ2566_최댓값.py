lis = []
for _ in range(9):
    lis.append(list(map(int,input().split())))
    
max_list = [max(a) for a in lis]
max_val = max(max_list)

row_index = max_list.index(max_val)
col_index = lis[row_index].index(max_val)
print(max_val)
print(row_index+1, col_index+1)
