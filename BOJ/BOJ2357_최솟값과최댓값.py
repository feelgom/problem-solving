#%%
from math import inf
import sys

def make_tree(start,end,node):
    if start == end:
        tree[node] = [numbers[start],numbers[start]]
        return tree[node]
    mid = (start+end)//2
    a = make_tree(start,mid,node*2)
    b = make_tree(mid+1,end,node*2+1)
    tree[node] = [min(a[0],b[0]), max(a[1],b[1])]
    return tree[node]

def get_minmax(start, end, node, left,right):
    if start>right or end<left:
        return [inf, -inf]
    if start>=left and end<=right:
        return tree[node]
    
    mid = (start+end)//2
    a = get_minmax(start,mid,node*2,left,right)
    b = get_minmax(mid+1,end,node*2+1,left,right)
    
    return [min(a[0],b[0]), max(a[1],b[1])]

# 단순 리스트로 만들시 시간초과가 발생한다.
# segment tree (구간합트리)를 만들어서 구하자

N, M = map(int,input().split())
numbers = []
for _ in range(N):
    num = int(sys.stdin.readline().strip())
    numbers.append(num)
length = len(numbers)
tree_length = 1
while tree_length <= length:
    tree_length *= 2
tree_length *= 2
tree = [[inf,-inf]]*tree_length

make_tree(0,N-1,1)
for _ in range(M):
    mi, ma = map(int, sys.stdin.readline().strip().split())
    ans = get_minmax(0,N-1,1, mi-1, ma-1)
    print(*ans)
