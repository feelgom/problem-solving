def preorder_traverse(tree, node):
    if node ==None:
        return ""
    left = tree[node].get('left',None)
    right = tree[node].get('right',None)
    ans = node
    ans += preorder_traverse(tree, left)
    ans += preorder_traverse(tree, right)
        
    return ans

def inorder_traverse(tree, node):
    if node ==None:
        return ""
    left = tree[node].get('left',None)
    right = tree[node].get('right',None)
    ans = inorder_traverse(tree, left)
    ans += node
    ans += inorder_traverse(tree, right)
        
    return ans

def postorder_traverse(tree, node):
    if node ==None:
        return ""
    left = tree[node].get('left',None)
    right = tree[node].get('right',None)
    ans = postorder_traverse(tree, left)
    ans += postorder_traverse(tree, right)
    ans += node
        
    return ans

N = int(input())
tree = {}
for _ in range(N):
    root, left, right = input().split()
    if left == ".":
        left = None
    if right == ".":
        right = None
    tree[root] = {"left":left, "right":right}
    
print(preorder_traverse(tree,"A"))
print(inorder_traverse(tree,"A"))
print(postorder_traverse(tree,"A"))
