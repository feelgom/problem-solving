a,b,c,d,e,f = map(int,input().split())
x = int((c*e - f*b) / (a*e - d*b))
y = int((c*d - f*a) / (b*d - e*a))
print(x,y)
