D,H,W = map(int,input().split())
a = D / (H**2 + W**2)**0.5
print(int(a*H),int(a*W))