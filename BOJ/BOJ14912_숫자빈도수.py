n,d=input().split()
a=0
for s in range(1,int(n)+1):
    a+=str(s).count(d)
print(a)