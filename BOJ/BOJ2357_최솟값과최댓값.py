#%%
# 단순 리스트로 만들시 시간초과가 발생한다.
# N, M = map(int,input().split())
N, M = 10, 4
numbers = [75,30, 100,38,50,51,52,20,81,5]
# for _ in range(N):
#     numbers.append(int(input()))


# for _ in range(M):
    # min_, max_ = map(int, input().split())
    # lis2 = numbers[min_-1:max_]
    # print(min(lis2), max(lis2))
    
# segment tree (구간합트리)를 만들어서 구하자
length = len(numbers)
i = 0
while 2**i <= length:
    i+=1
tree_length = 2**(i+1)
tree = [0]*tree_length

def make_tree(start,end,node):
    if start == end:
        tree[node] = numbers[start]
        return tree[node]
    mid = (start+end)//2
    
    tree[node] = make_tree(start,mid,node*2)+ make_tree(mid+1,end,node*2+1)
    return tree[node]

def tree_sum(start,end, node, left,right):
    if start>right or end<left:
        return 0
    if start>=left and end<=right:
        return tree[node]
    
    mid = (start+end)//2
    return tree_sum(start,mid,node*2,left,right) + tree_sum(mid+1,end,node*2+1,left,right)

make_tree(0,M-1,1)

